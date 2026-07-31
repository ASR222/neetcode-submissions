class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
            if count > max_count:
                max_count = count
        return max_count