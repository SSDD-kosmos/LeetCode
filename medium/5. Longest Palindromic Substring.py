# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        temporary_str = ''
        res_str = ''
        while len(s) > 0:
            for el in s:
                temporary_str += el
                if temporary_str == temporary_str[::-1]:
                    if len(res_str) < len(temporary_str):
                        res_str = temporary_str
            temporary_str = ''
            s = s[1:]
        return res_str


s = Solution()
print(s.longestPalindrome("bb"))
