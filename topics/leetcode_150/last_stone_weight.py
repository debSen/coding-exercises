import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        minheap = [item*-1 for item in stones]
        
        limit = 1
        
        heapq.heapify(minheap)
        while len(minheap) > limit:
            heaviest = heapq.heappop(minheap)
            secondheaviest = heapq.heappop(minheap)
            if heaviest != secondheaviest:
                remaining = secondheaviest - heaviest
                heapq.heappush(minheap, remaining*-1)
        minheap.append(0)
        return abs(minheap[0])
                