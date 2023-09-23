class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p *= nums[i]
        p = 1
        for j in range(n-1,-1,-1):
            output[j] *= p
            p *= nums[j]
        return output