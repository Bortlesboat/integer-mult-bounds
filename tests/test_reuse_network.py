"""Independent finite checks for stage-sharing and its downstream substitution."""
from dataclasses import replace
from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from certify import A, certify_parameters, network
from reuse_network import (BIT_SAVING, certificate, counts, parameters,
                           scalar_model, triple_matching)
from make_reuse_patch import patched_files


def multiply(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]


def projector(t,h):
    # Independent direct formula for the rational orthogonal line projector.
    v=[Q(i in t) for i in range(h)]
    form=[[Q(i==j)-Q(1,9) for j in range(h)] for i in range(h)]
    dual=[sum(v[i]*form[i][j] for i in range(h)) for j in range(h)]
    norm=sum(x*y for x,y in zip(v,dual))
    return [[x*y/norm for y in dual] for x in v]


class StageReuse(unittest.TestCase):
    def test_matching_all_h46_roles_and_small_even_sizes(self):
        for h in (6,8,10,12,46):
            triples,pi=triple_matching(h)
            self.assertEqual(sorted(pi),list(range(len(triples))))
            for i,j in enumerate(pi):
                self.assertEqual(len(set(triples[i])&set(triples[j])),1)
        with self.assertRaises(ValueError):triple_matching(9)

    def test_nesting_orthogonality_in_rational_form(self):
        triples,pi=triple_matching(6)
        zero=[[0]*6 for _ in range(6)]
        for i,j in enumerate(pi):
            P=projector(triples[i],6); R=projector(triples[j],6)
            self.assertEqual(multiply(P,P),P)
            self.assertEqual(multiply(R,P),zero)
            self.assertEqual(multiply(P,R),zero)
        # The tensor inclusion E subset H follows from these zero products.

    def test_full_scalar_network_restores_shared_dirty_scratch(self):
        for seed in (1,17):
            out=scalar_model(6,seed)
            self.assertTrue(out['bank_exchange'])
            self.assertTrue(out['scratch_restored'])
            self.assertEqual(out['shared_side_roles'],144000)

    def test_counts_and_downstream_margins(self):
        old=network(46); new=counts()
        self.assertEqual(new['old_W']-new['W'],old['N']*old['zb'])
        self.assertEqual(new['old_s']-new['s'],(new['old_W']-new['W'])*old['m'])
        self.assertEqual(new['W']*new['m']-new['s'],old['N']-2*old['Lb'])
        self.assertEqual(new['eta'],Q(9,29015910268))
        cert=certificate()
        self.assertEqual(Q(cert['witness']['minimum_margin']),3*BIT_SAVING**2/70)
        p=parameters()
        self.assertEqual(1-p.sigma,A)
        self.assertLess(p.tau,p.sigma)
        # Old bit network cannot support the new saving with the supplied L.
        self.assertLess(old['eta_b'],BIT_SAVING*Q(5743,500))
        with self.assertRaises(ValueError):
            certify_parameters(replace(p,kappa=Q(1,2**74)),generalized_beta=True,
                               strict_margin=True,layout_model='nonadjacent')

    def test_combined_patch_switches_only_bit_interface(self):
        files=list(patched_files())
        self.assertEqual(len(files),7)
        for name,old,new in files:
            if name.endswith('03-motifs.tex'):
                self.assertIn(r'E\subset H',new)
                self.assertIn(r'\label{prop:reused-bit-interface}',new)
                self.assertIn('9475984020888000',new)
            elif name.endswith('04-swap.tex'):
                self.assertIn(r'$W=W_{\rm b}^*$ and $s=s_{\rm b}^*$',new)
                self.assertIn(r'1-\frac{27}{10^{12}}',new)
                self.assertNotIn('prop:bit-motif-interface',new)
            elif name.endswith('05-layers.tex'):
                self.assertIn(r'\sigma=1-\frac9{500000000000}',new)
                self.assertIn('prop:complex-motif-interface',new)
            elif name.endswith('08-assembly.tex'):
                self.assertIn(r'\sigma=1-a_{\rm c}',new)
                self.assertIn(r'\kappa=2^{-75}',new)
                self.assertIn(r'19a^2/20<a_{\rm c}',new)
                self.assertNotIn(r'\kappa=2^{-76}',new)


if __name__=='__main__':unittest.main()
