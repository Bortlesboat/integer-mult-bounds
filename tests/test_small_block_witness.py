from itertools import combinations
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from small_block_witness import certificate, color, dot2


class SmallBlockWitness(unittest.TestCase):
    def test_color_classes_are_disjoint_affine_planes(self):
        for normal in range(1, 8):
            for offset in (0, 1):
                plane = [x for x in range(8) if dot2(normal, x) == offset]
                self.assertEqual(len(plane), 4)
                self.assertTrue(all(color(t) == normal-1
                                    for t in combinations(plane, 3)))

    def test_explicit_rational_gram_for_all_three_signature_types(self):
        triples = list(combinations(range(8), 3))
        signatures = [(1, 1), (1, -1), (-1, -1)]
        ambient_diag = [x for c in range(7) for x in signatures[c % 3]]
        for s in triples:
            left = [2*color(s), 2*color(s)+1]
            self.assertNotEqual(ambient_diag[left[0]]*ambient_diag[left[1]], 0)
            for t in triples:
                if len(set(s) & set(t)) == 1:
                    right = [2*color(t), 2*color(t)+1]
                    self.assertTrue(all(ambient_diag[i]*int(i == j) == 0
                                        for i in left for j in right))

    def test_target_scope_and_negative_deficit(self):
        c = certificate()
        self.assertEqual(c['neighbor_pairs_checked'], 840)
        self.assertLess(int(c['network_deficit']), 0)
        self.assertEqual(len(set(c['colors'])), 7)


if __name__ == '__main__':
    unittest.main()
