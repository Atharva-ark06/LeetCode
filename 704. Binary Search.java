/**
 * LeetCode 704 — Binary Search
 *
 * Approach: The input array is sorted. Inspect the middle element and
 * discard the half that cannot contain the target. Continue until the
 * target is found or the search interval becomes empty.
 *
 * Time: O(log n).
 * Space: O(1).
 */
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
}
