"""LeetCode 2469 — Convert the Temperature.

Convert Celsius to Kelvin and Fahrenheit, returning both in that order.
Time: O(1); Space: O(1).
"""
from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.0
        return [kelvin, fahrenheit]


if __name__ == "__main__":
    solution = Solution()
    assert solution.convertTemperature(36.50) == [309.65, 97.7]
    assert solution.convertTemperature(0) == [273.15, 32.0]
    print("All sample tests passed.")
