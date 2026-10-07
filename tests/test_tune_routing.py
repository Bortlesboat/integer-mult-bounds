"""Regression checks for combining routing and variable stopping thresholds."""
from dataclasses import replace
from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
from certify import A, certify_parameters, dyadic, margins
from tune_routing import certificate, parameters, patched_files


class TunedRouting(unittest.TestCase):
    def test_witness_requires_both_extensions(self):
        p = parameters()
        self.assertEqual(Q(certificate()["witness"]["minimum_margin"]), 3*A*A/70)
        with self.assertRaisesRegex(ValueError, 'beta=1/2'):
            certify_parameters(p, strict_margin=True, layout_model="nonadjacent")
        with self.assertRaisesRegex(ValueError, 'crt_layout'):
            certify_parameters(p, generalized_beta=True, strict_margin=True)
        for bad, message in ((replace(p, beta=Q(1,2)), 'packed_overhead'),
                             (replace(p, epsilon=Q(1,20)), 'guard_width'),
                             (replace(p, kappa=dyadic(75)), 'absorption'),
                             (replace(p, kappa=3*A*A/70), 'absorption')):
            with self.assertRaisesRegex(ValueError, message):
                certify_parameters(bad, generalized_beta=True, strict_margin=True,
                                   layout_model="nonadjacent")

    def test_transfer_recipe_and_precision(self):
        for a in [A, Q(1,17), *[dyadic(k) for k in range(5,61)]]:
            p = parameters(a, 3*a*a/140)
            certify_parameters(p, generalized_beta=True, strict_margin=True,
                               layout_model="nonadjacent")
            g = margins(p, layout_model="nonadjacent")
            self.assertEqual(min(g.values()), 3*a*a/70)
            self.assertEqual(g['g4'], 20*a/21)
            self.assertEqual(g['g5'], Q(13,112))
            self.assertEqual(g['g6'], Q(299,336))
            self.assertEqual(p.tau*(1+p.c/p.beta), 1-a*a)
        p = parameters()
        self.assertEqual(p.epsilon*p.C1, Q(20,21))
        self.assertEqual(Q(1,4)+p.epsilon/2, Q(23,84))
        self.assertEqual(Q(1,2)+2*p.epsilon, Q(25,42))
        self.assertEqual(1-2*p.epsilon, Q(19,21))
        self.assertEqual(dyadic(76)/dyadic(78), 4)

    def test_combined_patch_includes_stopping_proof_and_setup(self):
        files = list(patched_files())
        self.assertEqual(len(files), 7)
        for name, old, new in files:
            if name.endswith('05-layers.tex'):
                self.assertNotIn(r'Fix \(\beta=1/2\)', new)
                self.assertIn(r'e^v<d^u', new)
                self.assertIn('guard-width argument below', new)
            if name.endswith('08-assembly.tex'):
                for required in [r'd^{21}\le b', r'e^{10}<d^9',
                                 r'\epsilon=\frac1{21}', r'\beta=\frac9{10}',
                                 r'\kappa=2^{-76}', r'\gamma<28d^2\sqrt b',
                                 r'g_4&=(1-\tau)(1-\epsilon)']:
                    self.assertIn(required, new)
                for stale in [r'd^{40}', r'b^{1/40}', r'2^{-78}', r'\frac{a^2}{80}']:
                    self.assertNotIn(stale, new)


if __name__ == '__main__':
    unittest.main()
