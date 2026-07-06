class Solution:
    def canJump(self, nums: List[int]) -> bool:
        v = len(nums) - 1
        d = 0

        for i in range(len(nums)):
            if d >= i:
                d = max(i + nums[i], d)
                if d >= v:
                    return True
        
        return False