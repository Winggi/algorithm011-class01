class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 投机取巧法：
        # nums1[m:m+n] = nums2
        # nums1.sort()

        # 三指针法（从后往前遍历）：
        if m == 0: nums1[:n] = nums2
        elif n == 0: return
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p >= 0:
            if (nums1[p1] > nums2[p2] and p1 != -1) or p2 == -1:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1

