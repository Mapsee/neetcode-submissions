class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = defaultdict(int)
        res = []

        for i in range(len(nums)):
            hsh[nums[i]] += 1
        
        hsh_sorted = dict(sorted(hsh.items(), key=lambda item: item[1], reverse=False))

        while k > 0:
            res.append(hsh_sorted.popitem()[0])
            k -= 1
        
        return res


            


        