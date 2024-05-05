# https://leetcode.com/problems/total-distance-traveled/description/

class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        result = 0
        while (mainTank >= 5 and additionalTank > 0):
            result += 50
            mainTank -= 4
            additionalTank -= 1

        if mainTank > 0:
            result += mainTank * 10

        return result


s = Solution()
print(s.distanceTraveled(9, 2))


