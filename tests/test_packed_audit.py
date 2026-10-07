"""Small independent checks supporting the scoped packed-movement audit."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_packed_movement import (ORDERS, C_on_bit, minimum_swaps,
    original_swap_count, permute, recurrence_example, retained_schedule)


class PackedMovementAudit(unittest.TestCase):
    def test_retained_layout_reaches_finite_schedule_optimum(self):
        for order in ORDERS:
            with self.subTest(order=order):
                self.assertEqual(len(retained_schedule(order)), minimum_swaps(order))
                expected = 6 if order[-1] == 'y' else 8
                self.assertEqual(minimum_swaps(order), expected)
                self.assertLessEqual(expected, original_swap_count(order))

    def test_basis_change_cannot_be_dropped_across_child(self):
        state = [1,0,0,0]
        conjugated = permute(C_on_bit(permute(state), 2))
        self.assertEqual(conjugated, C_on_bit(state, 3))
        self.assertNotEqual(conjugated, C_on_bit(state, 2))
        # P is an involution, but P C P is not C: adjacent inverse
        # cancellation does not justify commuting through the child.
        self.assertEqual(permute(permute(state)), state)

    def test_exact_recurrence_sum(self):
        for levels in range(1,12):
            for stop in range(levels+1):
                for K in (1,4,25,144):
                    with self.subTest(levels=levels, stop=stop, K=K):
                        direct, unrolled = recurrence_example(levels,stop,K)
                        self.assertEqual(direct, unrolled)


if __name__ == '__main__':
    unittest.main()
