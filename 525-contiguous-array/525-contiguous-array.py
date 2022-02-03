class Solution:
    # def findMaxLength(self, nums: List[int]) -> int:
    #     dict = {0: 0}
    #     key, maxLen = 0, 0
    #     for i in range(len(nums)):
    #         key += nums[i] or -1
    #         if key not in dict:
    #             dict[key] = i + 1
    #         else:
    #             maxLen = max(maxLen, i + 1 - dict[key])
    #     return maxLen
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        key, maxLen = 0, 0
        for i in range(len(nums)):
            n = nums[i]
            if n == 0: 
                key -= 1
            else:
                key += 1
            if key in d:
                maxLen = max(maxLen, i - d[key])
            else:
                d[key] = i
        return maxLen