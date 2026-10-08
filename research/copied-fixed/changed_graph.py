"""Exact specialization of RaD / hipotures PR41 changed producer.

Alternating global pair order: point_order_search.py at rad checkpoint
7e488e6b25dc1713c1f41baaf1cefbf677507cf3. Trees: support-right at23,
left at25. Original envelope frames and descending donor matching are
certified separately. Underlying scalar generators: icekylinx PR18/36.
"""
from partial_swap.paired import PairedExclusionCircuit
from partial_swap.shared import SharedPointCircuit


def alternating_points(h,common):
    pairs=[(a,a+1) for a in range(0,h-1,2) if common not in (a,a+1)]
    if common%2:
        pairs.reverse()
    head=[x for pair in pairs for x in pair]
    return head+[x for x in range(h) if x!=common and x not in head]


def graph(h):
    assert h in (23,25)
    class Changed(PairedExclusionCircuit):
        base_threshold=2
        def total(self,values):
            values=[x for x in values if x]
            if h==23:
                values.sort(key=lambda node:(self.support[node].bit_count(),self.support[node]),reverse=True)
            result=0
            for node in values:
                result=self.add(result,node)
            return result
    local=Changed(h-1)
    total=local.pair(list(range(h-1)))[0]
    local.outputs[()]=total
    stack=[total]
    while stack:
        node=stack.pop()
        if not node or node in local.active:
            continue
        local.active.add(node)
        if local.args[node]:
            stack.extend(local.args[node])
    local.additions=sum(local.args[node] is not None for node in local.active)
    return SharedPointCircuit(h,local,point_order=alternating_points)
