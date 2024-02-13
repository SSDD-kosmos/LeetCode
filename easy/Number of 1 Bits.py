# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bit_count = 0
        while n != 0:
            n &= (n - 1)
            set_bit_count += 1
        return set_bit_count


s = Solution()
print(s.hammingWeight(11111111111111111111111111111101))
