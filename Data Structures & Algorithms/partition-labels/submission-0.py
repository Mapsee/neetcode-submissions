class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        letterCounts = defaultdict(int)
        count = 0
        ss = set()

        for c in s:
            letterCounts[c] += 1
        
        for c in s:
            ss.add(c)
            count += 1
            letterCounts[c] -= 1

            if letterCounts[c] == 0:
                ss.remove(c)
            
            if not ss:
                res.append(count)
                count = 0

        return res