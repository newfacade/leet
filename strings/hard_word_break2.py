from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        返回所有这些可能的单词拆分
        key: 记忆化搜索
        lru_cache可以记录函数的调用结果，再次使用时直接使用之前的返回值，而不真的再次调用
        """

        @lru_cache(None)
        def backtrack(index: int) -> List[List[str]]:
            """s[index:]'s represents by wordDict, in reverse order"""
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans

        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]
