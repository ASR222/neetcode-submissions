class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0]*n

        for i in range(n):
            RightMax = -1
            for j in range(i+1, n):
                RightMax = max(RightMax, arr[j])
            ans[i] = RightMax
        return ans
                
        




        