class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_l = 0

        seen = {}

        for right in range(len(s)):
            ch = s[right]
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            seen[ch] = right
            max_l = max(max_l, right - left +1)

        return max_l