class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum = 0

        for i in range(len(gas)):
            sum += gas[i] - cost[i]
        
        if sum < 0:
            return -1

        tank = 0
        start = 0
        i = 0
        
        while i < len(gas):
            if gas[i] + tank >= cost[i]:
                tank += gas[i] - cost[i]
                i += 1
            else:
                start += 1
                i = start
                tank = 0
        
        return start
