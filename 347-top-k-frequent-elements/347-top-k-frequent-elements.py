class Solution:
    def topKFrequent(self, nums, k):
        result = list()
        count = Counter(nums)
        max_heap = [(-val, key) for key, val in count.items()]
        heapq.heapify(max_heap)
        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])
        return result 