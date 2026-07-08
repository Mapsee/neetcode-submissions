class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        tank = 0
        start = 0
        i = 0
        passed = 0
        sum = 0
        
        while i < len(gas):
            if i == passed:
                sum += gas[i] - cost[i]
                passed += 1
            if gas[i] + tank >= cost[i]:
                tank += gas[i] - cost[i]
                i += 1
            else:
                start += 1
                i = start
                tank = 0

        if sum < 0:
            return -1
        
        return start
