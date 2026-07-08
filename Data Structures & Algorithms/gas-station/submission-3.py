class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_ = 0

        for i in range(len(gas)):
            sum_ += gas[i] - cost[i]
        
        if sum_ < 0:
            return -1

        tank = 0
        start = 0
        i = 0
        
        while i < len(gas):
            if gas[i] + tank >= cost[i]:
                tank += gas[i] - cost[i]
            else:
                start = i + 1
                tank = 0
            i += 1
        
        return start
