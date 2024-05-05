# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        counter = 0
        for n in nums:
            if counter < 0:
                return False
            elif n > counter:
                counter = n
            counter -= 1
            
        return True
            
        
s = Solution()
nums = [3,2,1,0,4]
print(s.canJump(nums))
