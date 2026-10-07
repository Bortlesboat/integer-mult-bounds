"""Paired circuits and the separate proof hypotheses needed for kappa=2^-59."""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from certify import certify_parameters,network
from exclusion_circuit import ExclusionCircuit
from paired_exclusion_circuit import PairedExclusionCircuit
from paired_network import certificate,circuit,parameters,guard_certificate,KAPPA
from dag_network import exact_invocation,shared_scalar_model
from reuse_network import triple_matching
from make_paired_patch import patched_files

class PairedNetwork(unittest.TestCase):
    def test_all_pair_coefficients_and_both_frames(self):
        for n in (4,5,8,13,25,49):
            c=PairedExclusionCircuit(n)
            self.assertTrue(c.verify()['all_output_supports_exact'])
            self.assertTrue(c.verify_embedding()['reverse_support_frames_nested'])
        self.assertEqual(c.additions,9813)

    def test_weighted_recursion_independently(self):
        for n in (5,6,9,13):
            c=PairedExclusionCircuit.__new__(PairedExclusionCircuit)
            inputs=[(i,) for i in range(n)]+list(combinations(range(n),2))
            c.support=[0]+[1<<i for i in range(len(inputs))]
            c.args=[None]*len(c.support);c.lookup={s:i for i,s in enumerate(c.support)}
            ids={p:i+1 for i,p in enumerate(inputs)}
            total,one,two=c.block(list(range(n)),{p:z for p,z in ids.items() if len(p)==2},
                                  {p[0]:z for p,z in ids.items() if len(p)==1})
            for omitted,node in [((),total)]+[((i,),z) for i,z in one.items()]+list(two.items()):
                expected=sum(1<<i for i,p in enumerate(inputs) if not set(p)&set(omitted))
                self.assertEqual(c.support[node],expected)

    def test_global_map_dirty_scratch_and_stage_matching(self):
        for h in (6,8):
            c=circuit(h);self.assertTrue(c.verify()['all_partial_outputs_exact'])
            self.assertTrue(c.verify_frames()['reverse_complement_frames_nested'])
            code=c.program()
            for inverse in (False,True):self.assertTrue(exact_invocation(h,inverse,code)['exact_linear_map'])
        code=circuit(6).program()
        for seed in (1,109):self.assertTrue(shared_scalar_model(6,seed,code)['bank_exchange'])
        triples,images=triple_matching(50)
        self.assertEqual(len(set(images)),19600)
        self.assertTrue(all(len(set(t)&set(triples[j]))==1 for t,j in zip(triples,images)))

    def test_stopped_depth_against_the_unrolled_recurrence(self):
        for beta in (Q(9,10),Q(999,1000)):
            cert=guard_certificate(beta=beta);m=cert['m'];s=int(cert['complex_s']);E=int(cert['E']);B=int(cert['B'])
            for k in (1,2,4):
                power=beta.denominator*k;d=m**power
                j=(1-beta)*power
                self.assertEqual(j.denominator,1)
                j=int(j)+1
                leaf=m**(power-j)
                depth=8*leaf*s**j+E*(s**j-1)//(s-1)
                # The proof gives depth <=9*B^2*d^(7/5); raise to the fifth power.
                self.assertLessEqual(depth**5,(9*B*B)**5*d**7)
                layer_depth=(m-1)*(1+power)*depth+18*d
                self.assertLess(layer_depth,int(cert['C0'])*d*d)

    def test_new_parameters_require_both_proof_extensions(self):
        p=parameters()
        with self.assertRaises(ValueError):certify_parameters(p,generalized_beta=True,strict_margin=True,layout_model='nonadjacent')
        with self.assertRaises(ValueError):certify_parameters(p,generalized_beta=True,strict_margin=True,layout_model='nonadjacent',guard_model='stopping')
        with self.assertRaises(ValueError):certify_parameters(replace(p,beta=Q(1,2)),generalized_beta=True,strict_margin=True,layout_model='nonadjacent',guard_model='stopping',assembly_model='tight-gaussian')
        c=certificate()
        self.assertEqual(int(c['bit_counts']['side_roles_per_invocation']),509194)
        self.assertEqual(c['global_circuit']['additions'],450394)
        self.assertEqual(Q(c['bit_counts']['eta']),Q(23,661055000))
        self.assertEqual(Q(c['witness']['minimum_margin']),Q(272158569,156250000000000000000000000))
        self.assertGreater(Q(c['witness']['minimum_margin']),KAPPA)
        self.assertLess(Q(c['witness']['minimum_margin'])/KAPPA,Q(101,100))
        self.assertLess(Q(c['fixed_network_ceiling']['value']),Q(1,2**58))

    def test_patch_updates_all_three_dependencies(self):
        files=list(patched_files());self.assertEqual(len(files),7)
        for name,old,new in files:
            if name.endswith('03-motifs.tex'):
                self.assertIn('h=50',new)
                self.assertIn(r'\label{prop:paired-bit-interface}',new)
                self.assertEqual(new.count(r'\label{eq:explicit-motif-exponents}'),1)
            elif name.endswith('04-swap.tex'):
                self.assertIn(r'$W=W_{\rm b}^{\rm pair}$ and $s=s_{\rm b}^{\rm pair}$',new)
            elif name.endswith('05-layers.tex'):
                self.assertIn(r'\label{sec:stopped-guard}',new)
                self.assertIn('46184298777878576000000',new)
                self.assertNotIn('C_1=20',new)
            elif name.endswith('08-assembly.tex'):
                for literal in (r'\kappa=2^{-59}',r'(32db)^{1/4}',r'd^{1000}\le b^{199}',r'g_5=1/4-\delta-5\epsilon/4',r'b\ge2^{40}'):
                    self.assertIn(literal,new)
                for obsolete in ('12d^2b','2^{24}','2^{-111}','1/4+\\epsilon/2','C_1=20'):
                    self.assertNotIn(obsolete,new)

if __name__=='__main__':unittest.main()
