# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder: return
        root_id = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_id])
        root.left = self.buildTree(preorder, inorder[:root_id])
        root.right = self.buildTree(preorder, inorder[root_id + 1:])
        return root