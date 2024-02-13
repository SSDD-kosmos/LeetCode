# https://leetcode.com/problems/sqrtx/description/
from math import sqrt


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))


s = Solution()
print(s.mySqrt(8))

