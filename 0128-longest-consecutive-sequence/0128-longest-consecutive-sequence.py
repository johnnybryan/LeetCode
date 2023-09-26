class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heap, temp, res = list(set(nums)), 0, 0
        heapq.heapify(heap)
        
        while heap:
            popped = heapq.heappop(heap)
            temp += 1
            if heap == [] or heap[0] != popped + 1:
                res = max(temp, res)
                temp = 0
        return res
            
            