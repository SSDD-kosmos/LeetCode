# https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        map1, map2 = {}, {}
        if len(pattern) != len(words):
            return False
        for st, w in zip(pattern, words):
            if st in map1 and map1[st] != w:
                return False
            if w in map2 and map2[w] != st:
                return False
            map1[st] = w
            map2[w] = st

        return True


s = Solution()
print(s.wordPattern('abbb', 'dog cat cat dog'))

