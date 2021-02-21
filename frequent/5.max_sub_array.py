from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        动态规划、nums[i]改为包含原nums[i]的最大sub-array和
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)
