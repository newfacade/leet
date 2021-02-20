from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """在未排序的数组中找到第 k 个最大的元素"""
        nums.sort()
        return nums[-k]
