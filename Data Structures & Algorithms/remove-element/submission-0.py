class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        counter = 0
        for r in range(0, len(nums)):
            if nums[r] == val:
                counter += 1
            else:
                nums[l] = nums[r]
                l += 1
        
        return len(nums) - counter
        