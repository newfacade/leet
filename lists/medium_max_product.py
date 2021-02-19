from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组，返回乘积
        key: 在没有0的情况下, 最大子数组一定是从一端开始的
        中间乘积最大且为负数 -> 两边为负 -> 有负负得正 -> 矛盾
        中间乘积最大且为正数 -> 两边为负，不然可拓展 -> 可拓展至整个数组 -> 矛盾
        """
        prefix, suffix, res = 0, 0, nums[0]
        for i in range(len(nums)):
            prefix = nums[i] if not prefix else nums[i]*prefix
            suffix = nums[-i - 1] if not suffix else nums[-i - 1]*suffix
            res = max(res, prefix, suffix)
        return res

