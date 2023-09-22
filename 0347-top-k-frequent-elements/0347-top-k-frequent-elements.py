class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map, heap, top_k_els = {}, [], []
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        for key, val in freq_map.items():
            heapq.heappush(heap, (-val, key))
        for _ in range(k):
            item = heapq.heappop(heap)
            top_k_els.append(item[1])
        return top_k_els
            
        