class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = len(set(s))
        while st:
            for i in range(len(s) - st + 1):
                if len(set(s[i:i+st])) == st:
                    return st
            st -= 1

        return st