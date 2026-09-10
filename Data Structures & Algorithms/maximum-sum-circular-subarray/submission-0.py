class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        MAX = []
        n = len(nums)
        nums = nums + nums
        

        for i in range(n):
            maxsum = nums[i]
            cursum = 0

            for j in range(i, i+n):
                if cursum < 0:
                    cursum = 0
                cursum += nums[j]
                maxsum = max(maxsum, cursum)
            MAX.append(maxsum)

        return max(MAX)




        