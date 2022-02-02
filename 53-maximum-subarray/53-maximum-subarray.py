# DP
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp = [0]*len(nums)
#         dp[0] = nums[0]
#         for i in range(1, len(nums)):
#             dp[i] = max(dp[i-1] + nums[i], nums[i])
#         return max(dp)

# KADANE'S ALGO
   
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = nums[0]
        for i in range(1,len(nums)):
            currSum += nums[i]
            currSum = max(currSum, nums[i])
            maxSum  = max(maxSum, currSum)
            
        return maxSum