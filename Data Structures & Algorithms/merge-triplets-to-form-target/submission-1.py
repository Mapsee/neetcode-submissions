class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = []

        for t in triplets:
            if cur == []:
                updateCur = True
                for i in range(3):
                    if t[i] > target[i]:
                        updateCur = False
                        break
                if updateCur:
                    cur = t

            else:
                new = [max(t[0], cur[0]), max(t[1], cur[1]), max(t[2], cur[2])]
                updateCur = True

                for i in range(3):
                    if t[i] > target[i]:
                        updateCur = False
                        break
                
                if updateCur:
                    cur = new
        
        return cur == target