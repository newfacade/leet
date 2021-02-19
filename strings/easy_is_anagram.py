import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词
        use collections.Counter
        """
        return collections.Counter(s) == collections.Counter(t)
