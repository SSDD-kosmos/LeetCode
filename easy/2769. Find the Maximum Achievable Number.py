# https://leetcode.com/problems/find-the-maximum-achievable-number/description/

class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        return num + t * 2


s = Solution()
print(s.theMaximumAchievableX(4, 1))

