class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sums = []
        last_sum = 0
        i = 0
        while (i < len(nums)):
            last_sum += nums[i]
            running_sums.append(last_sum)
            i += 1
        return running_sums