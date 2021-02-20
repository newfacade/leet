from typing import List
import math


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        给定一个数组，将数组中的元素向右移动 k 个位置
        利用最大公约数，环状替换
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        gcd = math.gcd(n, k)
        for i in range(gcd):
            pre_num = nums[i]
            for j in range(n // gcd):
                index = (i + (j + 1) * k) % n
                tmp = nums[index]
                nums[index] = pre_num
                pre_num = tmp

