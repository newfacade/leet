import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1
        use collections.Counter
        """
        count = collections.Counter(s)
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
