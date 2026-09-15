class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)

        for i in range(len(nums)):
            pair = target - nums[i]

            if pair in d:
                return [d[pair], i]
            
            d[nums[i]] = i

        