class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)

        for i, num in enumerate(nums):
            pair = target - num
            
            if pair in d:
                return [d[pair], i]
            
            d[num] = i

        