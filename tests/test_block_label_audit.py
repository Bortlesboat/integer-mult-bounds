"""Independent finite checks of the spectral and local-pairing audit."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_block_labels import (certificate, incidence_eigenvalues,
                               log_rational_bounds, neighbor_spectrum)
from search_network import log_integer_bounds


class BlockLabelAudit(unittest.TestCase):
    def test_johnson_eigenvalues_by_direct_integer_action(self):
        for h in (6,7,8,9):
            triples=[set(t) for t in combinations(range(h),3)]
            for j in range(4):
                # Degree-j harmonic from j disjoint coordinate pairs.
                f=[]
                for T in triples:
                    x=1
                    for i in range(j):x*=int(2*i in T)-int(2*i+1 in T)
                    f.append(x)
                self.assertTrue(any(f))
                for t in range(4):
                    eigenvalue=incidence_eigenvalues(h,t)[j]
                    actual=[sum(comb(len(S&T),t)*x for T,x in zip(triples,f))
                            for S in triples]
                    self.assertEqual(actual,[eigenvalue*x for x in f])

    def test_positive_semidefinite_dual_exact_spectrum(self):
        spectrum=neighbor_spectrum(24)
        self.assertEqual(spectrum,[630,150,-37,3])
        v=comb(24,3);b=Q(v,667);t=37*b
        self.assertEqual(t+b*spectrum[0]-v,0)
        self.assertTrue(all(t+b*x>=0 for x in spectrum[1:]))
        self.assertEqual(Q(v)/t,Q(667,37))

    def test_local_pairing_forces_incompatible_zero_sum_planes(self):
        K=[[Q(8,9),-Q(1,9),-Q(1,9)],
           [-Q(1,9),-Q(1,9),-Q(1,9)],
           [-Q(1,9),-Q(1,9),-Q(1,9)]]
        kernel=[0,1,-1]
        self.assertEqual([sum(a*b for a,b in zip(row,kernel)) for row in K],[0,0,0])
        self.assertNotEqual(K[0][0]*K[1][1]-K[0][1]*K[1][0],0)
        u=[1,-1,0]
        self.assertEqual(sum(u[i]*K[i][j]*u[j] for i in range(3) for j in range(3)),1)

    def test_exact_boundaries_and_log_normalization(self):
        for m in (1,2,17,97336):
            self.assertEqual(log_rational_bounds(Q(m)),log_integer_bounds(m))
        c=certificate()
        self.assertEqual(c['intersection_only_blocks']['minimum_ambient_rank'],48)
        self.assertEqual(c['positive_definite_labels']['h24_rank_two_dimension_lower'],37)
        self.assertEqual(c['characteristic_two']['ambient_rank_lower'],169)
        self.assertIn('OPEN',c['unrestricted_target_status'])


if __name__=='__main__':unittest.main()
