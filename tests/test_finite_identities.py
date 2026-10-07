"""Independent finite checks of selected upstream identities.

These test small instances and adversarial boundary values. They do not prove
the large network's rank interfaces or a Turing-machine running-time bound.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
import random
import unittest


def eight_steps(u, w, c):
    u -= c*(w % 2 == 0)
    w -= c*(u % 2 == 0)
    u += c*(w % 2 == 0)
    w += c*(u % 2 == 0)
    w += c*(u % 2 == 1)
    u += c*(w % 2 == 1)
    w -= c*(u % 2 == 1)
    u -= c*(w % 2 == 1)
    return u, w


def packed_steps(x, y, z, K, f, rho, inverse=False):
    # Targets, signs, and tested parity, in the manuscript's chronological order.
    lines = [("y", -1, 0), ("z", -1, 0), ("y", 1, 0), ("z", 1, 0),
             ("z", 1, 1), ("y", 1, 1), ("z", -1, 1), ("y", -1, 1)]
    values = {"y": y, "z": z}
    modulus = 1 << (K*f)
    for target, sign, parity in (reversed(lines) if inverse else lines):
        other = values["z" if target == "y" else "y"]
        offset = sum(1 << j for j in (rho+i*K for i in range(f-1))
                     if (x >> j) & 1 and ((other >> j) & 1) == parity)
        values[target] = (values[target] + (-sign if inverse else sign)*offset) % modulus
    return x, values["y"], values["z"]


def is_bad(y, z, K, f, rho):
    mask = (1 << (K-1))-1
    return any(not 10 <= ((v >> (rho+i*K+1)) & mask) <= (1 << (K-1))-11
               for v in (y, z) for i in range(f-1))


class FiniteIdentities(unittest.TestCase):
    def test_scalar_eight_step_gadget_including_negative_integers(self):
        for u, w, c in product(range(-16, 17), range(-16, 17), range(2)):
            self.assertEqual(eight_steps(u, w, c), (u+c*(1-2*(u % 2)), w))

    def test_packed_gadget_guard_and_exception_invariance(self):
        rng = random.Random(109)
        good = bad = 0
        for K, f in ((6, 2), (6, 3), (8, 3), (10, 4)):
            modulus = 1 << (K*f)
            for rho in range(K):
                for _ in range(150):
                    x, y, z = (rng.randrange(modulus) for _ in range(3))
                    actual = packed_steps(x, y, z, K, f, rho)
                    self.assertEqual(packed_steps(*actual, K, f, rho, inverse=True), (x, y, z))
                    exceptional = is_bad(y, z, K, f, rho)
                    self.assertEqual(is_bad(actual[1], actual[2], K, f, rho), exceptional)
                    if not exceptional:
                        mask = sum(((x >> j) & 1) << j
                                   for j in (rho+i*K for i in range(f-1)))
                        self.assertEqual(actual, (x, y ^ mask, z))
                        good += 1
                    else:
                        # Repair maps a current exceptional address to the ideal image
                        # of its preimage, so it must recover the exact selected XOR.
                        preimage = packed_steps(*actual, K, f, rho, inverse=True)
                        mask = sum(((preimage[0] >> j) & 1) << j
                                   for j in (rho+i*K for i in range(f-1)))
                        self.assertEqual((preimage[0], preimage[1] ^ mask, preimage[2]),
                                         (x, y ^ mask, z))
                        bad += 1
        self.assertGreater(good, 1000)
        self.assertGreater(bad, 1000)

    def test_neighbor_counts_and_scalar_cancellation(self):
        for h in (7, 10):
            triples = [set(t) for t in combinations(range(h), 3)]
            for S in triples:
                bit = complex_count = 0
                for T in triples:
                    intersection = len(S & T)
                    bit_side = int(intersection == 1)
                    bit += bit_side
                    self.assertEqual((intersection+bit_side) % 2, int(S == T))
                    coefficient = Q(intersection-1, 2)
                    neighbor = S != T and intersection % 2 == 0
                    complex_count += neighbor
                    self.assertEqual(coefficient-(coefficient if neighbor else 0), int(S == T))
                self.assertEqual(bit, 3*comb(h-3, 2))
                self.assertEqual(complex_count, comb(h-3, 3)+3*(h-3))

    def test_signed_centered_packing_against_direct_convolution(self):
        rng = random.Random(109)
        for r in (2, 4, 8, 16):
            for _ in range(50):
                p = 5
                a = [rng.randint(-2**p, 2**p) for _ in range(r)]
                b = [rng.randint(-2**p, 2**p) for _ in range(r)]
                # All convolution coefficients have absolute value < base/2.
                width = 2*p + r.bit_length() + 2
                base = 1 << width
                A = sum(x*base**j for j, x in enumerate(a))
                B = sum(x*base**j for j, x in enumerate(b))
                value = A*B
                extracted = []
                for _ in range(2*r-1):
                    digit = value % base
                    if digit >= base//2:
                        digit -= base
                    extracted.append(digit)
                    value = (value-digit)//base
                direct = [sum(a[i]*b[j-i] for i in range(r) if 0 <= j-i < r)
                          for j in range(2*r-1)]
                self.assertEqual(extracted, direct)
                self.assertEqual(value, 0)


if __name__ == "__main__":
    unittest.main()
