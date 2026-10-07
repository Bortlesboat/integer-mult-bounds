"""Exact checks for shared intermediate computations and reversible embedding."""
from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from exclusion_circuit import ExclusionCircuit
from dag_network import BIT_SAVING,certificate,counts,exact_invocation,shared_scalar_model
from incidence_rectangles import rectangles
from search_incidence_partitions import rich,certificate as partition_certificate
from make_dag_patch import patched_files


class SharedComputation(unittest.TestCase):
    def test_richer_partition_remains_an_exact_partition(self):
        for n in range(4,11):
            seen=set();p=rich(n);c=l=r=0
            for S,T in rectangles(p):
                c+=1;l+=len(S);r+=len(T)
                for s in S:
                    for t in T:
                        self.assertFalse(set(s)&set(t))
                        self.assertNotIn((s,t),seen);seen.add((s,t))
            self.assertEqual((c,l,r),(p.count,p.left,p.right))
            self.assertEqual(len(seen),n*(n-1)*(n-2)*(n-3)//4)
        bound=partition_certificate()['fixed_h46_flat_rectangle_bound']
        self.assertLess(Q(bound['kappa_upper']),Q(1,2**60))

    def test_all_coefficients_and_both_frame_directions(self):
        for n in (4,5,7,10,17,45):
            c=ExclusionCircuit(n)
            self.assertTrue(c.verify()['all_output_supports_exact'])
            e=c.verify_embedding()
            self.assertTrue(e['forward_support_frames_nested'])
            self.assertTrue(e['reverse_support_frames_nested'])
            self.assertEqual(e['reversible_roles'],c.additions+len(c.outputs))

    def test_forward_and_reverse_on_every_dirty_input_basis_vector(self):
        for h in (6,8):
            for inverse in (False,True):
                self.assertTrue(exact_invocation(h,inverse)['exact_linear_map'])

    def test_entire_three_stage_shared_scratch_network(self):
        for seed in (1,109):
            result=shared_scalar_model(seed=seed)
            self.assertEqual(result['roles'],counts(6)['W'])
            self.assertTrue(result['bank_exchange'] and result['all_scratch_restored'])

    def test_strict_witness_and_preserved_rank_deficit(self):
        c=certificate();n=counts()
        self.assertEqual(c['circuit']['additions'],11566)
        self.assertEqual(c['circuit']['nonzero_coefficients'],893970)
        self.assertEqual(n['side_roles_per_invocation'],577576)
        self.assertEqual(n['eta'],Q(27,1254369032))
        self.assertEqual(n['W']*n['m']-n['s'],572394081600)
        self.assertEqual(Q(c['witness']['minimum_margin']),3*BIT_SAVING**2/70)
        self.assertGreater(Q(c['witness']['minimum_margin']),Q(1,2**63))

    def test_patch_connects_the_new_interface_and_preserves_complex(self):
        files=list(patched_files())
        self.assertEqual(len(files),7)
        for name,old,new in files:
            if name.endswith('03-motifs.tex'):
                self.assertIn(r'\label{prop:dag-bit-interface}',new)
                self.assertEqual(new.count(r'\label{eq:explicit-motif-exponents}'),1)
            elif name.endswith('04-swap.tex'):
                self.assertIn('prop:dag-bit-interface',new)
                self.assertIn(r'$W=W_{\rm b}^{\rm dag}$ and $s=s_{\rm b}^{\rm dag}$',new)
            elif name.endswith('05-layers.tex'):
                self.assertIn('prop:complex-motif-interface',new)
                self.assertIn(r'\sigma=1-\frac9{500000000000}',new)
            elif name.endswith('08-assembly.tex'):
                self.assertIn(r'\kappa=2^{-63}',new)
                self.assertIn(r'Put $a=187/10^{11}$',new)


if __name__=='__main__':unittest.main()
