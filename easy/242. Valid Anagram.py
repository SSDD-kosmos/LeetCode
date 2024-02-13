# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
