# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res_str = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', s).lower()
        if res_str == res_str[::-1]:
            return True
        return False


s = Solution()
print(s.isPalindrome("0P"))

