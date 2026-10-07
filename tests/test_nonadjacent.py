"""Finite counterexample searches for the direct-axis proof and its witnesses.

The swap primitives' fixed-tape running-time bounds remain upstream assumptions.
"""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import permutations, product
from math import prod
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"scripts"))
from certify import BASELINE, certify_parameters, margins
from make_nonadjacent_patch import layout_only_files, result_files
from nonadjacent import (apply_primitive, certificate, inverse_schedule, parameters,
                        permute_records, swap_schedule)


def named_bits(widths):
    return [(axis, bit) for axis, width in enumerate(widths)
            for bit in reversed(range(width))]


def flat_index(coordinates, sizes):
    index = 0
    for value, size in zip(coordinates, sizes):
        index = size*index+value
    return index


def direct_oracle(records, widths, i, j):
    """Independent mixed-radix specification, without using bit primitives."""
    sizes = [1 << width for width in widths]
    new_sizes = sizes.copy()
    new_sizes[i], new_sizes[j] = new_sizes[j], new_sizes[i]
    result = [None]*len(records)
    for coordinates in product(*(range(s) for s in sizes)):
        output = list(coordinates)
        output[i], output[j] = output[j], output[i]
        result[flat_index(output, new_sizes)] = records[flat_index(coordinates, sizes)]
    return result


def axis_map(records, widths, axis, matrix, valid_bounds):
    """Expose one axis, apply an exact rectangular map, zero pad, and restore."""
    schedule = swap_schedule(widths, axis, len(widths)-1)
    exposed = permute_records(records, widths, schedule)
    order = list(range(len(widths)))
    order[axis], order[-1] = order[-1], order[axis]
    sizes = [1 << widths[i] for i in order]
    line_size = sizes[-1]
    output = []
    for line, prefix in enumerate(product(*(range(s) for s in sizes[:-1]))):
        values = exposed[line*line_size:(line+1)*line_size]
        valid = all(value < valid_bounds[name] for name, value in zip(order[:-1], prefix))
        if valid:
            output.extend(sum((coefficient*values[j] for j, coefficient in enumerate(row)), Q(0))
                          for row in matrix)
            output.extend([Q(0)]*(line_size-len(matrix)))
        else:
            output.extend([Q(0)]*line_size)
    return permute_records(output, [widths[i] for i in order], inverse_schedule(schedule))


class NonadjacentAudit(unittest.TestCase):
    def test_bit_schedules_all_positions_width_patterns_and_inverse(self):
        for d in range(1, 7):
            for widths in product((0, 1), repeat=d):
                # Also test nonempty fields with one-bit difference and a large gap.
                for offset in (0, 1, 5):
                    ws = [w+offset for w in widths]
                    bits = named_bits(ws)
                    for i in range(d):
                        for j in range(d):
                            expected = list(range(d))
                            expected[i], expected[j] = expected[j], expected[i]
                            oracle = [(axis, bit) for axis in expected
                                      for bit in reversed(range(ws[axis]))]
                            schedule = swap_schedule(ws, i, j)
                            self.assertLessEqual(len(schedule), 2)
                            actual = bits
                            for step in schedule:
                                actual = apply_primitive(actual, step)
                            self.assertEqual(actual, oracle)
                            for step in inverse_schedule(schedule):
                                actual = apply_primitive(actual, step)
                            self.assertEqual(actual, bits)

    def test_exhaustive_payload_permutations_against_tuple_oracle(self):
        for d in range(1, 5):
            for widths in product((1, 2), repeat=d):
                # Distinct non-palindromic payloads detect reversal or coefficient mixing.
                records = [(i, -i-7, 2*i+1) for i in range(1 << sum(widths))]
                for i in range(d):
                    for j in range(d):
                        actual = permute_records(records, widths, swap_schedule(widths, i, j))
                        self.assertEqual(actual, direct_oracle(records, widths, i, j))

    def test_crt_reversal_and_control_order(self):
        for d in range(1, 6):
            for widths in product((1, 2), repeat=d):
                records = list(range(1 << sum(widths)))
                current, ws = records, list(widths)
                for i in range(d//2):
                    j = d-1-i
                    current = permute_records(current, ws, swap_schedule(ws, i, j))
                    ws[i], ws[j] = ws[j], ws[i]
                self.assertEqual(ws, list(reversed(widths)))
                sizes = [1 << w for w in widths]
                for coordinates in product(*(range(s) for s in sizes)):
                    target = flat_index(list(reversed(coordinates)), list(reversed(sizes)))
                    self.assertEqual(current[target], records[flat_index(coordinates, sizes)])
                # After reversing (a_d,...,a_1), all lower-index controls precede i.
                names = list(reversed(range(d)))
                for i in range(d//2):
                    j = d-1-i
                    names[i], names[j] = names[j], names[i]
                for i in reversed(range(d)):
                    self.assertTrue(all(names.index(j) < names.index(i) for j in range(i)))

    def test_padded_expansion_and_compression_all_axis_orders(self):
        widths = (1, 2, 1)
        sizes, source = (2, 4, 2), (1, 3, 1)
        coordinates = list(product(*(range(t) for t in sizes)))
        data = [Q(1+sum((j+1)*x for j, x in enumerate(coord)), 16)
                if all(x < s for x, s in zip(coord, source)) else Q(0)
                for coord in coordinates]
        # Dense exact contractions with distinct coefficients, not identities.
        expansion = [[[Q(1+i+j, 32) for j in range(s)] for i in range(t)]
                     for s, t in zip(source, sizes)]
        compression = [[[Q(2+2*i+j, 64) for j in range(t)] for i in range(s)]
                       for s, t in zip(source, sizes)]
        for order in permutations(range(3)):
            expanded, bounds = data, list(source)
            for axis in order:
                expanded = axis_map(expanded, widths, axis, expansion[axis], bounds)
                bounds[axis] = sizes[axis]
                for value, coord in zip(expanded, coordinates):
                    if any(x >= b for x, b in zip(coord, bounds)):
                        self.assertEqual(value, 0)
            expected = [sum((data[flat_index(src, sizes)] *
                             prod(expansion[k][dest[k]][src[k]] for k in range(3))
                             for src in product(*(range(s) for s in source))), Q(0))
                        for dest in coordinates]
            self.assertEqual(expanded, expected)
            compressed, bounds = expanded, list(sizes)
            for axis in reversed(order):
                compressed = axis_map(compressed, widths, axis, compression[axis], bounds)
                bounds[axis] = source[axis]
                for value, coord in zip(compressed, coordinates):
                    if any(x >= b for x, b in zip(coord, bounds)):
                        self.assertEqual(value, 0)
            expected = [sum((expanded[flat_index(src, sizes)] *
                             prod(compression[k][dest[k]][src[k]] for k in range(3))
                             for src in coordinates), Q(0))
                        if all(x < s for x, s in zip(dest, source)) else Q(0)
                        for dest in coordinates]
            self.assertEqual(compressed, expected)

    def test_full_padded_crt_routing_and_inverse(self):
        # Independent CRT oracle: exponent k maps to (mu_i*k mod s_i)_i.
        for source in ((3, 5, 7), (7, 3, 5)):
            widths = [s.bit_length() for s in source]
            sizes = [1 << w for w in widths]
            prefix = [prod(source[:i]) for i in range(len(source))]
            mu = [pow(prefix[i], -1, source[i]) for i in range(len(source))]
            coordinates = list(product(*(range(s) for s in sizes)))
            data = []
            for reversed_coord in product(*(range(t) for t in reversed(sizes))):
                coord = list(reversed(reversed_coord))
                data.append(1+sum(x*p for x, p in zip(coord, prefix))
                            if all(x < s for x, s in zip(coord, source)) else 0)
            original = data.copy()
            reverse_widths = list(reversed(widths))
            # Three axes need one endpoint transposition, including unequal widths.
            data = permute_records(data, reverse_widths, swap_schedule(reverse_widths, 0, 2))
            for inverse in (False, True):
                axes = range(3) if inverse else reversed(range(3))
                for axis in axes:
                    output = [None]*len(data)
                    for coord in coordinates:
                        dest = list(coord)
                        if all(coord[j] < source[j] for j in range(axis+1)):
                            offset = mu[axis]*sum(coord[j]*prefix[j] for j in range(axis))
                            dest[axis] = (coord[axis]+(-offset if inverse else offset)) % source[axis]
                        output[flat_index(dest, sizes)] = data[flat_index(coord, sizes)]
                    data = output
                if not inverse:
                    expected = [0]*len(data)
                    for k in range(prod(source)):
                        dest = [mu[i]*k % source[i] for i in range(3)]
                        expected[flat_index(dest, sizes)] = k+1
                    self.assertEqual(data, expected)
            data = permute_records(data, widths, swap_schedule(widths, 0, 2))
            self.assertEqual(data, original)
            self.assertEqual([x for x in data if x], list(range(1, prod(source)+1)))

    def test_new_witnesses_need_new_layout_and_keep_precision_slack(self):
        self.assertEqual(set(certificate()["cases"]), {"frozen", "h46"})
        for name in ("frozen", "h46"):
            p = parameters(name)
            with self.assertRaisesRegex(ValueError, 'crt_layout'):
                certify_parameters(p, strict_margin=True)
            g = margins(p, layout_model="nonadjacent")
            self.assertEqual(min(g.values()), (1-p.tau)**2/80)
            self.assertEqual(g["g4"], Q(39,40)*(1-p.tau))
            self.assertEqual(g["g5"], Q(3,20))
            self.assertEqual(g["g6"], Q(73,80))
            self.assertEqual(g["g7"], Q(1,40))
            for bad in (replace(p, epsilon=Q(1,20)), replace(p, kappa=min(g.values()))):
                with self.assertRaises(ValueError):
                    certify_parameters(bad, strict_margin=True, layout_model="nonadjacent")
        with self.assertRaisesRegex(ValueError, 'Unknown layout model'):
            certify_parameters(BASELINE, layout_model="typo")

    def test_patches_preserve_analytic_d_squared_and_complete_layout_changes(self):
        variants = [list(layout_only_files()), list(result_files("frozen")),
                    list(result_files("h46"))]
        self.assertEqual([len(v) for v in variants], [2, 4, 7])
        for files in variants:
            for name, old, new in files:
                if name.endswith("07-resampling.tex"):
                    self.assertIn("$2(d-1)$", new)
                    self.assertNotIn(r"d^2(1+\ell^\tau)", new)
                    self.assertIn("undo precisely that interchange", new)
                if name.endswith("08-assembly.tex"):
                    self.assertNotIn(r"\epsilon(2-\tau)", new)
                    self.assertNotIn(r"d^2(1+\ell^\tau)", new)
                    self.assertIn(r"\gamma<28d^2\sqrt b", new)
                    self.assertIn(r"(12d^2b)^{1/4}", new)
                    self.assertIn(r"\log(8d^2\log x)", new)
                    self.assertIn(r"\epsilon(1-\tau)<1-\tau", new)
        for name, old, new in variants[-1]:
            if name.endswith("08-assembly.tex"):
                self.assertIn(r"d^{40}\le b", new)
                self.assertIn(r"\epsilon=\frac1{40}", new)
                self.assertIn(r"\kappa=2^{-78}", new)
                self.assertNotIn(r"b^{\frac{27}{2000000000000}}", new)


if __name__ == '__main__':
    unittest.main()
