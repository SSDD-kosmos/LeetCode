# https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        counter, max_jump, end = 0, 0, 0
        
        if len(nums) == 1:
            return 0
        elif nums[0] >= len(nums) - 1:
            return 1

        for i in range(len(nums) - 1):
            max_jump = max(max_jump, i + nums[i])
            if max_jump >= len(nums) - 1:
                counter += 1
                break
            if i == end:
                counter += 1
                end = max_jump

        return counter
            
                    
s = Solution()
nums = [1, 1, 1, 1]

print(s.jump(nums))
