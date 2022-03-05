class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        n = len(nums)
        hash_map = dict()
        
        for i in range(n - 1):
            if nums[i] == key:
                if nums[i+1] not in hash_map:
                    hash_map[nums[i+1]] = 1
                else:
                    hash_map[nums[i+1]] += 1
        
        max_count = max(hash_map.values())
        
        for target in hash_map:
            if hash_map[target] == max_count:
                return target