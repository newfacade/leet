class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        给定一个字符串，验证它是否是回文串
        key: 双指针, isalnum()
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():  # Return True if the string is an alpha-numeric string, False otherwise.
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
