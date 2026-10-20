from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque(i for i, party in enumerate(senate) if party == "R")
        dire = deque(i for i, party in enumerate(senate) if party == "D")
        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"
