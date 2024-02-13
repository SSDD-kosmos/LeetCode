# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1

        return nums


s = Solution()
print(s.moveZeroes([1, 0, 0, 0, 2]))
