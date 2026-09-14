class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in hm:
                return [hm[to_find], i]

            # if num not in hm:
            hm[num] = i

        