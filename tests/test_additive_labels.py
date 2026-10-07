"""Independent finite checks of the point-additive obstruction."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_additive_labels import certificate, neighbor_rows, rank_mod


def rational_rank(rows):
    rows = [[Q(x) for x in row] for row in rows]
    pivot_row = 0
    for col in range(len(rows[0])):
        found = next((i for i in range(pivot_row, len(rows)) if rows[i][col]), None)
        if found is None:
            continue
        rows[pivot_row], rows[found] = rows[found], rows[pivot_row]
        scale = rows[pivot_row][col]
        rows[pivot_row] = [x/scale for x in rows[pivot_row]]
        for i in range(pivot_row+1, len(rows)):
            if rows[i][col]:
                scale = rows[i][col]
                rows[i] = [x-scale*y for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


class AdditiveLabelAudit(unittest.TestCase):
    def test_neighbor_annihilator_and_rank_over_rationals(self):
        for h in range(6, 11):
            for target in ((0, 1, 2), (0, h-2, h-1)):
                rows = neighbor_rows(h, target)
                vector = [3*int(i in target)-1 for i in range(h)]
                self.assertTrue(all(sum(x*y for x, y in zip(row, vector)) == 0
                                    for row in rows))
                self.assertEqual(rational_rank(rows), h-1)

    def test_scalar_fitting_rank_and_exceptional_h9(self):
        for h in range(6, 11):
            triples = [set(t) for t in combinations(range(h), 3)]
            gram = [[len(s & t)-1 for t in triples] for s in triples]
            self.assertEqual(rational_rank(gram), h-int(h == 9))
            self.assertEqual(rank_mod(gram), h-int(h == 9))

    def test_block_column_changes_preserve_rank(self):
        # Arbitrary invertible right factors, including nonsymmetric blocks.
        triples = [set(t) for t in combinations(range(6), 3)]
        matrix = []
        for s in triples:
            for a in range(2):
                row = []
                for j, t in enumerate(triples):
                    C = [[1, j], [1, j+1]]
                    row.extend((len(s & t)-1)*C[a][b] for b in range(2))
                matrix.append(row)
        self.assertEqual(rational_rank(matrix), 12)

    def test_certificate_scope(self):
        c = certificate()
        self.assertEqual(c['target_ambient_rank_lower'], 48)
        self.assertEqual(c['unrestricted_indefinite_rank_two_target'], 'OPEN')


if __name__ == '__main__':
    unittest.main()
