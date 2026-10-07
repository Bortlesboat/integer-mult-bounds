"""Checks for the formulas used in bounded alternative-network screens."""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from certify import network
from search_network_variants import unequal_counts
from block_label_targets import hypothetical_counts, target
from reuse_network import counts


class NetworkVariants(unittest.TestCase):
    def test_block_label_arithmetic_is_explicitly_hypothetical(self):
        old=counts(); lifted=hypothetical_counts(46,46,1)
        for key in ('W','m','L','eta'):
            self.assertEqual(lifted[key],old[key])
        doubled=hypothetical_counts(46,92,2)
        # Merely duplicating every old label does not improve eta.
        self.assertEqual(doubled['eta'],old['eta'])
        candidate=hypothetical_counts(24,24,2)
        self.assertEqual(candidate['eta'],Q(37,551741760))
        out=target()
        self.assertIn('UNREALIZED',out['status'])
        self.assertEqual(Q(out['hypothetical_parameter_check']['minimum_margin']),
                         Q(21,10**19))

    def test_unequal_formula_specializes_to_original_counts(self):
        for h in (15,38,39,46,60,100,200):
            n=network(h)
            self.assertEqual(unequal_counts((h,h,h)),
                             (n['N'],n['m'],n['Wb'],n['N']-2*n['Lb']))
        for hs in permutations((39,46,70)):
            self.assertEqual(unequal_counts(hs),unequal_counts((39,46,70)))

    def test_positive_deficit_implies_tail_screen_hypotheses(self):
        # Direct integer formulas, including the first allowed ground size.
        for h in range(4,15):
            self.assertGreaterEqual(Q(12*h,(h-1)*(h-2)),1)
        for hs in ((39,46,70),(15,299,299),(46,46,46),(60,70,300)):
            N,m,W,D=unequal_counts(hs)
            if D>0:
                self.assertLess(sum(Q(1,h) for h in hs),Q(1,12))
                self.assertGreater(m,36**3)

    def test_direct_sum_representation_has_edges_but_fails_stage_nesting(self):
        # This tempting 3h-dimensional representation preserves local graph
        # orthogonality, but an earlier full-factor span is not orthogonal to
        # the next target line. Test actual vectors and the proposed form.
        h=7
        def u(a,b,c):
            return [Q(i in t) for t in (a,b,c) for i in range(h)]
        def inner(x,y):
            return sum(a*b for a,b in zip(x,y))-Q(7,81)*sum(x)*sum(y)
        A={0,1,2}; R={0,3,4}; S={0,1,2}; T={0,3,4}; C={1,5,6}
        target=u(A,S,C)
        self.assertEqual(inner(target,target),2)
        self.assertEqual(inner(u(A,T,C),target),0)
        self.assertEqual(inner(u(R,T,C),target),-2)


if __name__=='__main__':unittest.main()
