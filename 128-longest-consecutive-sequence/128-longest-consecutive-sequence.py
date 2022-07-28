class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest, cur_long = 0, min(1, len(nums))
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] : continue
            if nums[i] == nums[i - 1] + 1: cur_long += 1
            else: longest, cur_long = max(longest, cur_long), 1
        return max(longest, cur_long)
            
            