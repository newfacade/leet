from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串
        key: 回溯算法
        """
        result = []

        def helper(cur_s: str, pre_palindromes: List[str]):
            """proceed like a tree"""
            if not cur_s:
                result.append(pre_palindromes)
            for i in range(1, len(cur_s) + 1):
                if cur_s[:i] == cur_s[:i][::-1]:
                    helper(cur_s[i:], pre_palindromes + [cur_s[:i]])

        helper(s, [])
        return result

