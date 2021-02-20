from typing import List
import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """给定两个数组，编写一个函数来计算它们的交集"""
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        ret = []
        for key in set(c1.keys()) & set(c2.keys()):
            ret.extend([key] * min(c1[key], c2[key]))
        return ret
