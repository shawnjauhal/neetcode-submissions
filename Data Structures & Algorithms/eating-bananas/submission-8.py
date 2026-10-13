class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = (l + r) // 2
        res = r
        while l <= r:
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            if time <= h:
                r = k - 1
                res = min(k, res)
                
            else:
                l = k + 1
            k = (l + r) // 2
        return res