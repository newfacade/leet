from typing import List


class Solution:
    """
    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素
    Boyer-Moore 投票算法
    if final_candidate != major:
    1. (major, *) period eliminated, each (major, major) correspond to a (major, other)
    2. (other, major) correspond to a (other, other)
    so #(major) = #(major, major) + #(other, major) <= #(major, other) + #(other, other) = #(other), contradiction!
    """
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
