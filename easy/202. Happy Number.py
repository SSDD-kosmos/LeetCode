# https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
def sumOfSquaredDigits(n):
    total_sum = 0
    while n > 0:
        digit = n % 10
        total_sum += digit * digit
        n = n // 10
    return total_sum

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sumOfSquaredDigits(n)
        return n == 1



s = Solution()
print(s.isHappy(77))

