import java.util.HashSet;
import java.util.Set;

/**
 * LeetCode 217 — Contains Duplicate
 *
 * Approach: Insert each number into a HashSet. If insertion is attempted
 * for a value already present, a duplicate exists and we can return true.
 *
 * Time: O(n) expected.
 * Space: O(n).
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }

        return false;
    }
}
