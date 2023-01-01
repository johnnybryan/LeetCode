class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = dict()
        for i in range(len(nums)):
            if nums[i] in cache:
                return True
            cache[nums[i]] = True
        return False