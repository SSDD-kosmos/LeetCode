# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
