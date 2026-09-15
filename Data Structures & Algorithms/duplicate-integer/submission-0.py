class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = defaultdict(int)

        for num in nums:
            if num in dups: 
                return True 
            dups[num] += 1
        
        return False
        