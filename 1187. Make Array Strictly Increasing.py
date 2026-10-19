from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2 = sorted(set(arr2))
        # Map the last chosen value to the minimum replacements used.
        states = {-1: 0}
        for value in arr1:
            next_states = {}
            for previous, cost in states.items():
                if value > previous:
                    next_states[value] = min(next_states.get(value, float("inf")), cost)
                index = bisect_right(arr2, previous)
                if index < len(arr2):
                    replacement = arr2[index]
                    next_states[replacement] = min(
                        next_states.get(replacement, float("inf")), cost + 1
                    )
            states = next_states
            if not states:
                return -1
            # For each value, lower replacement counts dominate higher counts.
            best = float("inf")
            pruned = {}
            for last in sorted(states):
                best = min(best, states[last])
                pruned[last] = states[last]
            states = pruned
        return min(states.values()) if states else -1
