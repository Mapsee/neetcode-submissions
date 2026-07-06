class Solution:
    def jump(self, nums: List[int]) -> int:
        d = 0
        c = 0
        l = r = 0

        while r < len(nums):
            if d >= len(nums) - 1:
                return c
            for j in range(l, r + 1):
                d = max(d, nums[j] + j)
            c += 1
            l = r + 1
            r = nums[j] + j

        return c
        