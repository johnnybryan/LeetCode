class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i and nums[i-1] >= nums[i]:
            i -= 1
        
        j = n - 1
        while j > i and i and nums[j] <= nums[i-1]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1