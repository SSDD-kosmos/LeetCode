# https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result_list = []
        sublist = []
        for i in range(len(nums)):
            try:
                if nums[i] + 1 == nums[i + 1]:
                    sublist.append(nums[i])
                elif nums[i] + 1 != nums[i + 1] and len(sublist) >= 1:
                    sublist.append(nums[i])
                    result_list.append(f'{sublist[0]}->{sublist[-1]}')
                    sublist = []
                elif nums[i] + 1 != nums[i + 1] and len(sublist) == 0:
                    result_list.append(f'{nums[i]}')
            except IndexError:
                if len(sublist) >= 1 and nums[-1] - 1 == sublist[-1]:
                    sublist.append(nums[i])
                    result_list.append(f'{sublist[0]}->{sublist[-1]}')
                else:
                    result_list.append(f'{nums[i]}')

        return result_list


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
