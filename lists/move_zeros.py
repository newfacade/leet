from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序
        使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                if left != right:
                    nums[left], nums[right] = nums[right], nums[left]  # 交换
                left += 1
            right += 1

