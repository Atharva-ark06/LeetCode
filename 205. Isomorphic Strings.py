"""LeetCode 205: Isomorphic Strings.

Two maps enforce a one-to-one mapping in both directions.
Time: O(n); Space: O(k), for the distinct characters.
"""


class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_to_t, t_to_s = {}, {}
        for left, right in zip(s, t):
            if s_to_t.get(left, right) != right or t_to_s.get(right, left) != left:
                return False
            s_to_t[left] = right
            t_to_s[right] = left
        return True


if __name__ == "__main__":
    solver = Solution()
    assert solver.isIsomorphic("egg", "add")
    assert not solver.isIsomorphic("foo", "bar")
    assert solver.isIsomorphic("paper", "title")
    print("All tests passed.")
