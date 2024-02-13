# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)

        for el in nums:
            if target > el:
                continue
            else:
                return nums.index(el)

        return len(nums)


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 2))
