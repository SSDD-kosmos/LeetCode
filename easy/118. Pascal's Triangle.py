# https://leetcode.com/problems/pascals-triangle/description/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res_list = []
        if numRows == 0:
            return res_list

        res_list.append([1])

        for i in range(1, numRows):
            prev_row = res_list[-1]
            current_row = [1]

            for ind in range(1, i):
                current_row.append(prev_row[ind - 1] + prev_row[ind])

            current_row.append(1)
            res_list.append(current_row)

        return res_list


s = Solution()
print(s.generate(4))
