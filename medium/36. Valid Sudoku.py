# https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(9):
            row_nums = set()
            col_nums = set()
            for x in range(9):
                if board[y][x] in row_nums or board[x][y] in col_nums:
                    return False
                if board[y][x] != '.':
                    row_nums.add(board[y][x])
                if board[x][y] != '.':
                    col_nums.add(board[x][y])

        for y in range(3):
            for x in range(3):
                nums = set()
                for yy in range(3):
                    for xx in range(3):
                        num = board[3 * y + yy][3 * x + xx]
                        if num in nums:
                            return False
                        if num != '.':
                            nums.add(num)

        return True


s = Solution()
print(s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                       [".", "9", "8", ".", ".", ".", ".", "6", "."],
                       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                       [".", "6", ".", ".", ".", ".", "2", "8", "."],
                       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
