class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev_min, prev_max, cur_min, cur_max, max_prod = nums[0], nums[0], nums[0], nums[0], nums[0]
        for n in nums[1:]:
            cur_min = min(prev_min*n, prev_max*n, n)
            cur_max = max(prev_min*n, prev_max*n, n)
            prev_min = cur_min
            prev_max = cur_max
            max_prod = max(max_prod, cur_max)
        return max_prod