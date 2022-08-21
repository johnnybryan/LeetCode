class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest, current = 0, min(1, len(nums))
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] : continue
            if nums[i] == nums[i - 1] + 1: current += 1
            else: longest, current = max(longest, current), 1
        return max(longest, current)
            