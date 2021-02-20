from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        给定一个整数数组，判断是否存在重复元素
        """
        return len(nums) != len(set(nums))
