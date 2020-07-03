class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归法：
        # res = []
        # def traverse(root):
        #     if root:
        #         res.append(root.val)
        #         traverse(root.left)
        #         traverse(root.right)
        # traverse(root)
        # return res
        
        # 非递归法：
        res = []
        stack = []
        while root or len(stack) > 0:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res