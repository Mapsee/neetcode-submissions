class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            rightSum = 0
            leftSum = 0
            for l in range(i):
                leftSum += nums[l]
            for r in range(i + 1, len(nums)):
                rightSum += nums[r]
            
            if leftSum == rightSum:
                return i
        
        return -1

        