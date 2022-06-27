from math import ceil

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        low = 1
        high = max(piles)
        res = high
        while low <= high:
            mid = int(low + (high - low)/2)
            hours = 0
            for item in piles:
                hours += ceil(item/mid)
            if hours <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res
