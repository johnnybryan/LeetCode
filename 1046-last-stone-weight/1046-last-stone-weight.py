class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * x for x in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = heapq.heappop(heap) 
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)
        
        if len(heap) == 0:
            return 0
        return -1 * heap[0]
                
        