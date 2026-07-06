class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handDict = defaultdict(int)
        for card in hand:
            handDict[card] += 1
        handKeys = sorted(handDict.keys())

        for k in handKeys:
            c = handDict[k]
            if c <= 0:
                continue
            for j in range(k, k + groupSize):
                if j not in handKeys:
                    return False
                if handDict[j] >= c:
                    handDict[j] -= c 
                else:
                    return False

        return True