class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)

        for i, num in enumerate(nums):
            if (pair := target - num) in d:
                return [d[pair], i]
            
            d[num] = i

        