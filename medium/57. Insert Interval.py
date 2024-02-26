# https://leetcode.com/problems/insert-interval/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result_list = []
        left = None
        right = None
        if not intervals:
            return [newInterval]

        for el in intervals:
            if newInterval[0] in range(el[0], el[1] + 1):
                left = el[0]
            elif left is None:
                left = newInterval[0]
            if newInterval[1] in range(el[0], el[1] + 1):
                right = el[1]
            elif right is None:
                right = newInterval[1]

        newInterval = [left, right]

        for el in intervals:
            if el[0] in range(left, right + 1) or el[1] in range(left, right + 1):
                if newInterval not in result_list:
                    result_list.append(newInterval)
            elif el[0] > left and newInterval not in result_list:
                result_list.append(newInterval)
                result_list.append(el)
            else:
                result_list.append(el)

        if newInterval not in result_list:
            result_list.append(newInterval)

        return result_list


# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         res = []
#         for i in range(len(intervals)):
#             if newInterval[1] < intervals[i][0]:
#                 res.append(newInterval)
#                 return res + intervals[i:]
#             elif newInterval[0] > intervals[i][1]:
#                 res.append(intervals[i])
#             else:
#                 newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
#
#         res.append(newInterval)
#
#         return res


s = Solution()
print(s.insert([[0, 5], [8, 9]], [3, 4]))
