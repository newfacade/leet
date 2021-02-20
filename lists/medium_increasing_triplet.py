from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列
        small为之前最小的数、mid为第二小的数
        """
        if len(nums) < 3:
            return False
        small, mid = float('inf'), float('inf')  # 初始为最大值
        for i in range(len(nums)):
            if nums[i] <= small:  # 当前数字小于small，更新small
                small = nums[i]
            elif nums[i] <= mid:  # 当前数字大于small，小于mid，更新mid
                mid = nums[i]
            elif nums[i] > mid:  # 当前数字大于mid
                return True
        return False
