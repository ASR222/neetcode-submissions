class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid_h(k):
            h = 0
            for i in range(len(piles)):
                if piles[i] % k != 0:
                    temp = piles[i] // k + 1
                    h += temp 
                else:
                    temp = piles[i] // k
                    h += temp
            return h

        L = 1
        R = max(piles)
        res = []

        while L<=R:
            mid = (L + R) // 2
            if valid_h(mid) <= h:
                res.append(mid)
                R = mid - 1
            else:
                L = mid + 1
        k = min(res)
        return k


        