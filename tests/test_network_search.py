from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from search_network import log_integer_bounds, log_ratio_bounds, search, parameter_ceiling


class NetworkSearch(unittest.TestCase):
    def test_log_series_remainder_and_range_reduction(self):
        self.assertEqual(log_ratio_bounds(Q(1)), (0, 0))
        lo, hi = log_ratio_bounds(Q(2))
        self.assertGreater(lo, Q(69, 100))
        self.assertLess(hi, Q(70, 100))
        self.assertEqual(log_integer_bounds(8), (3*lo, 3*hi))
        tighter_lo, tighter_hi = log_ratio_bounds(Q(2), terms=32)
        self.assertGreater(tighter_lo, lo)
        self.assertLess(tighter_hi, hi)

    def test_unique_optimum_and_infinite_tail(self):
        data = search()
        self.assertEqual(data["winner_h"], 46)
        self.assertEqual(data["largest_certified_dyadic_saving"], "2^-36")
        self.assertGreater(Q(data["saving_lower"]), Q(data["tail_saving_upper"]))
        self.assertEqual(set(map(int, data["finite_enclosures"])), set(range(40, 200)))

    def test_ceiling_with_separate_sigma_and_variable_beta(self):
        data = parameter_ceiling()
        self.assertEqual(data["bit_network_search"]["winner_h"], 46)
        self.assertLess(Q(data["kappa_upper"]), Q(1, 2**107))
        self.assertGreater(Q(data["witness_fraction_of_upper"]), Q(99, 100))


if __name__ == "__main__":
    unittest.main()
