# https://leetcode.com/problems/score-of-a-string/description/


class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """

        # result_sum = 0
        # for i in range(0, len(s)-1):
        #     result_sum += abs(ord(s[i]) - ord(s[i+1]))
        # return result_sum

        return sum([abs(ord(s[i]) - ord(s[i+1])) for i in range(0, len(s)-1)])


s = Solution()
print(s.scoreOfString("hello"))

