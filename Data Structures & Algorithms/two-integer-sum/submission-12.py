class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in dic.keys():
                return [dic[nums[i]], i]
            t = target - nums[i]
            dic[t] = i