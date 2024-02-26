# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[counter] = nums[i]
                counter += 1
        return counter


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
