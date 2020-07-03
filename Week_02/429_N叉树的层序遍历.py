"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        cur_layer = [root]  # 队列
        res = []
        while cur_layer:
            next_layer = []
            tmp_res = []
            for r in cur_layer:
                if r:
                    tmp_res.append(r.val)
                    next_layer.extend(r.children)
            res.append(tmp_res)
            cur_layer = next_layer
        return res