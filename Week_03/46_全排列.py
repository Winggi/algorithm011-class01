class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯，大部分题解用的是换位的方法，我的方法是一个个数添加进去
        def helper(cur, rest):
            if len(cur) == len(nums):
                res.append(cur[:])
            for i in range(len(rest)):
                cur.append(rest.pop(i))
                helper(cur, rest)
                rest.insert(i, cur.pop())
                # helper(cur + [rest[i]], rest[:i] + rest[i + 1:]) # 上面三行写成这一行也可以，这样也能叫回溯吗？空间复杂度有变化？
        res = []
        helper([], nums[:])
        return res