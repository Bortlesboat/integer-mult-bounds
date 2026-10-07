"""Regression checks for certificates and patch scope, not for the full theorem."""
from dataclasses import replace
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from certify import (BASELINE, balanced, certificates, certify_parameters, dyadic,
                     margins, near_supremum, network, proposed, pushed, A,
                     LOG_BOUND, certify_rational_network)
from make_patch import extended_files, patched_files, pushed_files


class Certificates(unittest.TestCase):
    def test_baseline_and_all_candidates(self):
        data = certificates()
        self.assertEqual(len(data["cases"]), 13)
        for k in (50, 42, 36):
            gs = margins(proposed(k))
            self.assertEqual(gs["g2"], dyadic(3*k+2))
            self.assertEqual(gs["g3"], dyadic(3*k+3))
            self.assertEqual(min(gs.values()), gs["g3"])
        self.assertEqual(min(margins(BASELINE).values()), dyadic(181))

    def test_balanced_and_near_supremum_candidates(self):
        for k in (50, 42, 36):
            a = dyadic(k)
            gs = margins(balanced(k))
            self.assertEqual(gs["g2"], gs["g3"])
            self.assertEqual(min(gs.values()), dyadic(3*k+2))
            p = near_supremum(k)
            self.assertGreater(p.kappa, balanced(k).kappa)
            supremum = a**3/(4+2*a)
            self.assertLess(p.kappa, supremum)
            self.assertGreater(p.kappa, Q(99, 100)*supremum)
            self.assertEqual(margins(p)["g2"], margins(p)["g3"])
            self.assertEqual(margins(p)["g2"], margins(p)["g4"])

    def test_balanced_patch_has_updated_equal_minima(self):
        for name, old, new in patched_files(True):
            self.assertIn(r"\kappa=2^{-153}", new)
            if name.endswith("08-assembly.tex"):
                self.assertIn(r"g_2=2^{-152},\quad g_3=2^{-152}", new)
                self.assertIn(r"\min_i g_i=2^{-152}=2\kappa", new)

    def test_extended_patches_update_dependencies(self):
        for k, h, log_bound in ((42, 100, 14), (36, 46, 12)):
            files = list(extended_files(k, h, log_bound))
            self.assertEqual(len(files), 6)
            for name, old, new in files:
                self.assertNotIn("2^{-50}", new)
                if name.endswith("08-assembly.tex"):
                    self.assertIn(f"\\kappa=2^{{-{3*k+3}}}", new)
                    self.assertIn(f"g_2=2^{{-{3*k+2}}},\\quad g_3=2^{{-{3*k+2}}}", new)
                if name.endswith("03-motifs.tex") and h == 46:
                    for value in ("h=46", "97336", "=-37/9", r"\frac{23}{55}",
                                  r"\frac{47}{110}", r"\binom{43}{2}",
                                  r"\frac{9}{43518487588}", r"\frac{7}{22253827054}"):
                        self.assertIn(value, new)
                    for stale in ("h=100", "97}", "539", "=-91/9"):
                        self.assertNotIn(stale, new)

    def test_reject_insufficient_slack(self):
        p = proposed(50)
        for bad in (replace(p, kappa=2*p.kappa),
                    replace(p, lam=p.tau*(1+2*p.c)),
                    replace(p, epsilon=dyadic(50)),
                    replace(p, lamp=p.lam)):
            with self.assertRaises(ValueError):
                certify_parameters(bad)

    def test_strict_margin_and_beta_boundaries(self):
        for variant in ("109", "108", "rational"):
            p = pushed(variant)
            cert = certify_parameters(p, generalized_beta=True, strict_margin=True)
            self.assertGreater(Q(cert["absorption_gap"]), 0)
            self.assertFalse(cert["all_margins_at_least_twice_kappa"])
            g = min(margins(p).values())
            self.assertEqual(g, p.epsilon*p.c*A)
            for bad in (replace(p, kappa=g), replace(p, kappa=g+dyadic(120)),
                        replace(p, beta=0), replace(p, beta=1)):
                with self.assertRaises(ValueError):
                    certify_parameters(bad, generalized_beta=True, strict_margin=True)
            if variant != "109":
                with self.assertRaises(ValueError):
                    certify_parameters(p, strict_margin=True)
            # Extra displayed bounds used by all pushed source patches.
            gs = margins(p)
            for key, bound in (("g1", Q(1,2)), ("g4", A/2000),
                               ("g5", Q(1,8)), ("g6", Q(1,2)), ("g7", A/2)):
                self.assertGreater(gs[key], bound)
                self.assertGreater(bound, g)

    def test_rational_recurrence_comparison(self):
        cert = certify_rational_network()
        self.assertLess(Q(cert["log_upper"]), LOG_BOUND)
        for slack in cert["deficit_slacks"].values():
            self.assertGreater(Q(slack), 0)

    def test_pushed_patch_dependencies(self):
        for variant in ("109", "108", "rational"):
            p = pushed(variant)
            files = list(pushed_files(variant))
            self.assertEqual(len(files), 6)
            for name, old, new in files:
                for stale in ("2^{-111}", "2^{-36}", "2^{-37}", "2^{37}"):
                    self.assertNotIn(stale, new)
                if name.endswith("08-assembly.tex"):
                    self.assertNotIn("1-2\\kappa", new)
                    self.assertIn(r"$\rho=G-\kappa>0$", new)
                    self.assertIn(f"d^{{{p.epsilon.denominator}}}\\le b^{{{p.epsilon.numerator}}}", new)
                if name.endswith("05-layers.tex") and variant != "109":
                    self.assertNotIn(r"\beta=\frac12", new)
                    self.assertNotIn(r"\beta=1/2", new)
                    self.assertIn(r"compare $e^v<d^u$", new)

    def test_original_counts_reproduced(self):
        n = network(100)
        self.assertEqual(n["Wb"], 177176569091445000000)
        self.assertEqual(n["Wc"], 1873807244643542670000)
        self.assertEqual(n["sc"], 1873807244636671267308000000)
        self.assertEqual(n["eta_b"], Q(339, 22587335000000))
        self.assertEqual(n["eta_c"], Q(73, 19906842167500))
        self.assertEqual(n["nu"], 11)

    def test_h46_counts(self):
        n = network(46)
        self.assertEqual(n["m"], 97336)
        self.assertEqual(n["eta_b"], Q(9, 43518487588))
        self.assertEqual(n["eta_c"], Q(7, 22253827054))
        self.assertEqual(n["C1"], 20)

    def test_rank_budget_from_individual_edge_rows(self):
        # Sum the edge-residual table by wire type, independently of telescoping.
        for h in (46, 100):
            n = network(h)
            for z, center, expected, extra_source in (
                    (n["zb"], h, n["sb"], n["N"]),
                    (n["zc"], h+1, n["sc"], 0)):
                total = extra_source
                for j in (1, 2, 3):
                    a, f = h**(j-1), h**(3-j)
                    # X and Y data wires each have the same total increase.
                    total += 2*n["N"]*((a-1)*(h-1)+(h-1))
                    # Per-invocation centers and ordered side wires.
                    total += n["v"]**2*center*((a-1)*h+3*h+a*h*(f-1))
                    side = (a-1)+((a-1)*(h-1)+1)+(h-2)+1+a*h*(f-1)
                    total += n["v"]**3*z*side
                self.assertEqual(total, expected)

    def test_old_intermediate_bounds_cannot_be_retained(self):
        p = proposed(50)
        self.assertGreater(p.tau*(1+2*p.c), 1-31*dyadic(55))
        self.assertLess(margins(p)["g4"], dyadic(51))
        self.assertGreater(margins(p)["g4"], dyadic(52))

    def test_patch_changes_only_three_files_and_no_old_literals_remain(self):
        files = list(patched_files())
        self.assertEqual(len(files), 3)
        for name, old, new in files:
            self.assertIn(r"\kappa=2^{-154}", new)
            self.assertNotIn(r"\kappa=2^{-182}", new)
            if name.endswith("08-assembly.tex"):
                for stale in ("2^{-75}", "2^{75}", "2^{-56}", "2^{-181}",
                              "2^{-129}", "31\\cdot2^{-55}"):
                    self.assertNotIn(stale, new)


if __name__ == "__main__":
    unittest.main()
