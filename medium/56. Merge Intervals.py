# https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
