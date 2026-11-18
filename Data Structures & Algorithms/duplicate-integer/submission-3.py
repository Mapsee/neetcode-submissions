class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)
        for num in nums:
            if dic[num] > 0:
                return True
            dic[num] += 1
        
        return False
        