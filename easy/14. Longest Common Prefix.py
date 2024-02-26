# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        counter = 0
        min_length = len(min(strs, key=len))

        if len(strs[0]) == 0:
            return ''

        while True:
            if min_length == len(prefix):
                return prefix
            temporary_variable = strs[0][counter]
            temp_counter = 0
            for el in strs:
                if el[counter] == temporary_variable:
                    temp_counter += 1

            counter += 1

            if temp_counter == len(strs):
                prefix += temporary_variable
            else:
                return prefix


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
