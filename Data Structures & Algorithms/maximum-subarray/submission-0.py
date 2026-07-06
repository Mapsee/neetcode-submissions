class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_arr_sum = 0 
        max_sum = nums[0]

        for i, num in enumerate(nums):
            curr_arr_sum = max(curr_arr_sum + num, num)
            max_sum = max(max_sum, curr_arr_sum)

        return max_sum