from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_scratch_pooling import certificate,optimistic_counts
from reuse_network import counts


class ScratchPooling(unittest.TestCase):
    def test_only_tiny_central_role_gain_remains_at_h46(self):
        p=optimistic_counts(46);current=counts()
        self.assertEqual(current['W']-p['W'],current['v']**2*46)
        self.assertEqual(p['D'],current['W']*current['m']-current['s'])
        self.assertLess(Q(current['W'],p['W']),Q(1000001,1000000))
        c=certificate()
        self.assertTrue(c['excludes_2_to_minus_74'])
        self.assertLess(Q(c['kappa_upper']),Q(1,2**74))

    def test_bad_joins_cannot_improve_best_zero_join_ratio(self):
        for W in range(3,18):
            for D in range(1,2*W):
                for R in range(1,W):
                    self.assertLessEqual(Q(D-2*R,W-R),Q(D,W))


if __name__=='__main__':unittest.main()
