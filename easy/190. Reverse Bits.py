# https://leetcode.com/problems/reverse-bits/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, 'b')
        n = n.zfill(32)

        return int(n[::-1], 2)


s = Solution()
print(s.reverseBits(11111111111111111111111111111101))

