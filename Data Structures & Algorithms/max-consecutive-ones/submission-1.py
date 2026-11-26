class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for num in nums:
            if num != 1:
                res = max(count, res)
                count = 0
            else: 
                count += 1
        
        return max(res, count)
        