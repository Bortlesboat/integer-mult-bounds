"""Independent finite checks of scoped network-search rejection bounds."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import random
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from research_networks import pair_common_neighbors, report


class ResearchScreens(unittest.TestCase):
    def test_pair_common_neighbors_by_enumeration(self):
        for h in range(6,11):
            triples=list(combinations(range(h),3))
            left={0,1,2}
            for k in range(3):
                right=set(range(k)) | set(range(3,6-k))
                actual=sum(len(left&set(t))==len(right&set(t))==1 for t in triples)
                self.assertEqual(actual,pair_common_neighbors(h,k))

    def test_subfamily_edge_identity_and_cauchy_bound(self):
        rng=random.Random(109)
        for h in range(6,11):
            full=list(combinations(range(h),3))
            for _ in range(12):
                family=rng.sample(full,rng.randrange(1,len(full)+1))
                v=len(family)
                point=[sum(i in t for t in family) for i in range(h)]
                pair=[sum(i in t and j in t for t in family)
                      for i,j in combinations(range(h),2)]
                E=sum(len(set(s)&set(t))==1 for s in family for t in family)
                self.assertEqual(E,sum(x*x for x in point)-2*sum(x*x for x in pair)+3*v)
                self.assertGreaterEqual(E,Q(9*v*v,h)-6*v*h+15*v)

    def test_hierarchy_channel_identity(self):
        triples=list(combinations(range(7),3))
        v=len(triples)
        adj=[{j for j,t in enumerate(triples) if len(set(s)&set(t))==1}
             for s in triples]
        internal=[]
        def make(leaves):
            if len(leaves)==1:return (set(leaves),None,None)
            mid=len(leaves)//2
            node=(set(leaves),make(leaves[:mid]),make(leaves[mid:]))
            internal.append(node[0]);return node
        tree=make(list(range(v)))
        def cover(node,neighbors):
            leaves,left,right=node
            if leaves<=neighbors:return 1
            if left is None:return 0
            return cover(left,neighbors)+cover(right,neighbors)
        count=sum(cover(tree,neighbors) for neighbors in adj)
        saved=sum(sum(leaves<=neighbors for neighbors in adj) for leaves in internal)
        self.assertEqual(count,sum(map(len,adj))-saved)

    def test_exact_scope_certificates(self):
        data=report()
        self.assertEqual(data['full_triples_bit_only']['finite_h_min'],39)
        self.assertTrue(data['hierarchical_aggregation']['excludes_2^-70'])
        self.assertEqual(data['triple_subfamilies']['winner_h'],46)
        self.assertEqual(Q(data['reuse_rejection']['h46_D_over_W']),Q(18,894191))
        for W in range(2,20):
            for D in range(1,2*W+1):
                for r in range(1,W):
                    self.assertLessEqual(Q(D-2*r,W-r),Q(D,W))


if __name__=='__main__':unittest.main()
