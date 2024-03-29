class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time: O(n), space: O(n)
        char_set = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest = max(r - l + 1, longest)
        return longest