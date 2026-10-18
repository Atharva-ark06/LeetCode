/*
 * LeetCode 9 — Palindrome Number
 *
 * Approach: Negative numbers cannot be palindromes, and positive numbers
 * ending in zero cannot be palindromes unless the number itself is zero.
 * Reverse only the second half of the digits, then compare the halves.
 * This avoids integer overflow from reversing the entire number.
 *
 * Time: O(log10(n)) — process about half the digits.
 * Space: O(1).
 */
#include <stdbool.h>

bool isPalindrome(int x) {
    if (x < 0 || (x != 0 && x % 10 == 0)) {
        return false;
    }

    int reversed_half = 0;

    while (x > reversed_half) {
        reversed_half = reversed_half * 10 + x % 10;
        x /= 10;
    }

    /* For odd digit counts, ignore the middle digit in reversed_half. */
    return x == reversed_half || x == reversed_half / 10;
}
