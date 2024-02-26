# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}

        for i in range(len(nums)):
            if nums[i] in num_dict and i - num_dict[nums[i]] <= k:
                return True
            num_dict[nums[i]] = i

        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
