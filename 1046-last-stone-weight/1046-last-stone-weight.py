class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            res = stones.pop() - stones.pop()
            stones.append(res)
            stones.sort()
        return stones[0]
            
                
        