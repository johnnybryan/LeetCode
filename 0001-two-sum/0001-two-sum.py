class Solution:
    def twoSum(self, nums: List[int], target_sum: int) -> List[int]:
        sum_map = {}
        for idx, val in enumerate(nums):
            target_val = target_sum - val
            if target_val in sum_map:
                return [sum_map[target_val], idx]
            sum_map[val] = idx