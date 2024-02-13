# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
