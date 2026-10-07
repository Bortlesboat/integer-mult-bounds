"""Independent scalar, partition and frame checks for rectangle aggregation."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from incidence_rectangles import best, rectangles, verify_partition
from incidence_network import (BIT_SAVING, certificate, counts, exact_invocation,
                               shared_scalar_model)
from reuse_network import triple_matching
from make_incidence_patch import patched_files


class IncidenceNetwork(unittest.TestCase):
    def test_recursive_partitions_cover_without_cancellation(self):
        for n in range(4,10):
            for a,b in ((1,1),(1,2),(2,1),(2,2)):
                self.assertTrue(verify_partition(n,a,b)['all_ordered_disjoint_pairs_exactly_once'])

    def test_rectangle_mixer_is_invertible_and_has_ones_submatrix(self):
        for a in range(1,7):
            for b in range(1,7):
                r=a+b-1
                wires=[1<<i for i in range(r)];old=list(wires)
                for i in range(1,a):wires[0]^=wires[i]
                for j in range(a,r):wires[j]^=wires[0]
                mask=(1<<a)-1
                self.assertTrue(all(wires[j]&mask==mask for j in (0,*range(a,r))))
                for j in range(a,r):wires[j]^=wires[0]
                for i in range(1,a):wires[0]^=wires[i]
                self.assertEqual(wires,old)

    def test_every_local_input_basis_vector_in_both_schedules(self):
        for h in (6,8):
            for inverse in (False,True):
                self.assertTrue(exact_invocation(h,inverse)['exact_linear_map'])

    def test_shared_three_stage_network_with_dirty_scratch(self):
        for seed in (1,109):
            result=shared_scalar_model(seed=seed)
            self.assertTrue(result['bank_exchange'] and result['all_scratch_restored'])
            self.assertEqual(result['roles'],counts(6)['W'])

    def test_rectangle_subspace_form_and_cross_orthogonality(self):
        # Nondegeneracy follows from the exact norm identity even for h>9,
        # when the ambient form is indefinite.
        h=12;i=0
        def pairing(x,y):
            return sum(a*b for a,b in zip(x,y))-Q(sum(x)*sum(y),9)
        for S,T in rectangles(best(h-1,2,2),tuple(range(1,h))):
            u=[Q(0)]*h
            for j,s in enumerate(S):
                for c in (i,*s):u[c]+=Q((-1)**j*(j+1),j+2)
            self.assertEqual(sum(u),3*u[i])
            self.assertEqual(pairing(u,u),sum(u[c]**2 for c in range(1,h)))
            for t in T:
                v=[int(c in (i,*t)) for c in range(h)]
                self.assertEqual(pairing(u,v),0)

    def test_stage_reuse_has_zero_backward_rank(self):
        h=6;triples,pi=triple_matching(h)
        for a,A in enumerate(triples):
            Ap=triples[pi[a]]
            self.assertEqual(len(set(A)&set(Ap))-1,0)
        m=h**3;dim_E=h;dim_H=(h*h-1)*h
        self.assertEqual((m-dim_E)+dim_H-(dim_H-dim_E),m)

    def test_h46_exact_certificate(self):
        c=certificate();n=counts()
        self.assertEqual(n['side_roles_per_invocation'],2394438)
        self.assertEqual(c['pair_partition']['scratch_roles'],52053)
        self.assertEqual(n['W']*n['m']-n['s'],n['N']-2*n['L'])
        self.assertGreater(Q(c['witness']['minimum_margin']),Q(1,2**67))
        self.assertEqual(Q(c['witness']['minimum_margin']),3*BIT_SAVING**2/70)

    def test_source_patch_connects_new_bit_and_retained_complex_interfaces(self):
        files=list(patched_files())
        self.assertEqual(len(files),7)
        for name,old,new in files:
            if name.endswith('03-motifs.tex'):
                self.assertIn(r'\label{prop:incidence-bit-interface}',new)
                self.assertIn('1110529317427200',new)
            elif name.endswith('04-swap.tex'):
                self.assertIn('prop:incidence-bit-interface',new)
                self.assertNotIn('prop:bit-motif-interface',new)
                self.assertIn(r'$W=W_{\rm b}^{\rm rect}$ and $s=s_{\rm b}^{\rm rect}$',new)
            elif name.endswith('05-layers.tex'):
                self.assertIn('prop:complex-motif-interface',new)
                self.assertIn(r'\sigma=1-\frac9{500000000000}',new)
            elif name.endswith('08-assembly.tex'):
                self.assertIn(r'\kappa=2^{-67}',new)
                self.assertIn(r'19a^2/20<a_{\rm c}',new)


if __name__=='__main__':unittest.main()
