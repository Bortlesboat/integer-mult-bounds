"""Cross-group support sharing, complement frames, and exact dirty-scratch maps."""
from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from shared_point_circuit import SharedPointCircuit
from shared_point_network import BIT_SAVING,KAPPA,certificate,counts
from dag_network import exact_invocation,shared_scalar_model
from make_shared_point_patch import patched_files

class CrossGroupSharing(unittest.TestCase):
    def test_every_support_and_both_frame_directions(self):
        for h in (6,8,10):
            c=SharedPointCircuit(h)
            self.assertTrue(c.verify()['every_node_has_common_point'])
            self.assertTrue(c.verify_frames()['reverse_complement_frames_nested'])
            # Independently expand every global support, without provenance.
            support=[0]*(len(c.args))
            for n in sorted(c.active):
                if c.args[n]:
                    a,b=c.args[n]
                    self.assertFalse(support[a]&support[b])
                    support[n]=support[a]|support[b]
                else:support[n]=1<<(n-1)
            for (common,target),n in c.outputs.items():
                expected=sum(1<<i for i,t in enumerate(c.inputs)
                             if set(t)&set(target)=={common})
                self.assertEqual(support[n],expected)

    def test_every_dirty_input_basis_vector_both_directions(self):
        for h in (6,8):
            code=SharedPointCircuit(h).program()
            for inverse in (False,True):
                self.assertTrue(exact_invocation(h,inverse,code)['exact_linear_map'])

    def test_entire_shared_three_stage_network(self):
        code=SharedPointCircuit(6).program()
        for seed in (1,109):
            result=shared_scalar_model(6,seed,code)
            self.assertEqual(result['roles'],counts(6)['W'])
            self.assertTrue(result['bank_exchange'] and result['all_scratch_restored'])

    def test_full_size_certificate_and_scope_of_ceiling(self):
        c=certificate()
        self.assertEqual(c['circuit']['additions'],486330)
        self.assertEqual(c['circuit']['merged_additions'],45706)
        self.assertEqual(int(c['bit_counts']['side_roles_per_invocation']),531870)
        self.assertEqual(int(c['bit_counts']['D']),572394081600)
        self.assertGreater(Q(c['witness']['minimum_margin']),KAPPA)
        self.assertEqual(Q(c['witness']['minimum_margin']),3*BIT_SAVING**2/70)
        self.assertEqual(KAPPA/Q(1,2**63),Q(13,8))
        self.assertLess(Q(c['exact_circuit_kappa_upper']),Q(1,2**62))

    def test_singular_ambient_form_is_rejected(self):
        with self.assertRaises(AssertionError):SharedPointCircuit(9)

    def test_patch_wires_the_new_interface_into_both_recurrences(self):
        files=list(patched_files())
        self.assertEqual(len(files),7)
        for name,old,new in files:
            if name.endswith('03-motifs.tex'):
                self.assertIn(r'\label{prop:shared-point-bit-interface}',new)
                self.assertEqual(new.count(r'\label{eq:explicit-motif-exponents}'),1)
            elif name.endswith('04-swap.tex'):
                self.assertIn('prop:shared-point-bit-interface',new)
                self.assertIn(r'$W=W_{\rm b}^{\rm shared}$ and $s=s_{\rm b}^{\rm shared}$',new)
            elif name.endswith('05-layers.tex'):
                self.assertIn(r'\tau=1-\frac{203}{10^{11}}',new)
                self.assertIn(r'\sigma=1-\frac9{500000000000}',new)
            elif name.endswith('08-assembly.tex'):
                self.assertIn(r'Put $a=203/10^{11}$',new)
                self.assertIn(r'\kappa=13\cdot2^{-66}',new)

if __name__=='__main__':unittest.main()
