class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = tank = 0
        for i, (fuel, expense) in enumerate(zip(gas, cost)):
            tank += fuel - expense
            if tank < 0:
                start, tank = i + 1, 0
        return start
