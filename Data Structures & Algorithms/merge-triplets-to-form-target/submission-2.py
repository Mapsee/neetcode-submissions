class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False

        for t in triplets:
            isValid = True 
            
            for i in range(3):
                if t[i] > target[i]:
                    isValid = False
                    break
            
            if isValid:
                if t[0] == target[0]:
                    x = True
                if t[1] == target[1]:
                    y = True
                if t[2] == target[2]:
                    z = True
            if x and y and z:
                return True
        
        return x and y and z 