class Solution:
    def twoSum(self, nums: List[int], target_sum: int) -> List[int]:
        sum_map = {}
        for idx, val in enumerate(nums):
            target_val = target_sum - val
            if target_val in sum_map:
                return [idx, sum_map[target_val]]
            sum_map[val] = idx
        