class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = defaultdict(int)
        res = []

        for num in nums:
            hsh[num] += 1
        
        arr = []
        for num,cnt in hsh.items():
            arr.append([cnt, num])
        arr.sort()
        
        while len(res) < k:
            res.append(arr.pop()[1])
        return res