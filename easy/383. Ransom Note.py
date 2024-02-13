# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for c in ransomNote:
            if c in count:
                count[c] -= 1
                if count[c] < 0:
                    return False
            else:
                return False
        return True


s = Solution()
print(s.canConstruct("aa", "aab"))
