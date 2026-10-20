from bisect import bisect_left
from itertools import accumulate
from random import randint

class Solution:
    def __init__(self, w: list[int]):
        self.prefix = list(accumulate(w))
        self.total = self.prefix[-1]

    def pickIndex(self) -> int:
        target = randint(1, self.total)
        return bisect_left(self.prefix, target)
