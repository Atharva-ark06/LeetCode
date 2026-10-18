// LeetCode 344: Reverse String
// Approach: Swap characters from both ends, moving inward.
// The character array is modified in place.
// Time: O(n) | Extra space: O(1)

class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;

        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}
