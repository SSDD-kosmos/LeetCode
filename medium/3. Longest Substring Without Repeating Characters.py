# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temporary_str = ''
        counter = 0
        counter_ind = 0
        while len(s) > 0:
            try:
                while s[counter_ind] not in temporary_str:
                    temporary_str += s[counter_ind]
                    counter_ind += 1
                else:
                    if counter < len(temporary_str):
                        counter = len(temporary_str)
                    temporary_str = ''
                    s = s[1:]
                    counter_ind = 0
            except IndexError:
                if counter < len(temporary_str):
                    counter = len(temporary_str)
                break
        return counter


s = Solution()
print(s.lengthOfLongestSubstring("asjrgapa"))
