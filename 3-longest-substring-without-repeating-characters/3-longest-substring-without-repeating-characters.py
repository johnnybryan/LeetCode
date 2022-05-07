class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, max_length = 0, 0, 0
        char_map = {}
        while end < len(s):
            last_char = s[end]
            if last_char in char_map:
                start = max(start, char_map[last_char] + 1)
            char_map[last_char] = end
            max_length = max(max_length, end - start + 1)
            end += 1
        return max_length