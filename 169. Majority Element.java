// LeetCode 169: Majority Element
// Approach: Boyer-Moore voting maintains a candidate and a vote balance.
// The problem guarantees that a majority element exists.
// Time: O(n) | Extra space: O(1)

class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int votes = 0;

        for (int value : nums) {
            if (votes == 0) {
                candidate = value;
            }
            votes += (value == candidate) ? 1 : -1;
        }

        return candidate;
    }
}
