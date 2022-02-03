class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict = {0: 0}
        key, maxLen = 0, 0
        for i in range(len(nums)):
            key += nums[i] or -1
            if key not in dict:
                dict[key] = i + 1
            else:
                maxLen = max(maxLen, i + 1 - dict[key])
        return maxLen