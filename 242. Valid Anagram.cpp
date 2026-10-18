#include <array>
#include <string>
using namespace std;

/*
 * LeetCode 242 — Valid Anagram
 *
 * Approach: Count each lowercase English letter in the first string,
 * then subtract counts while scanning the second string. Any negative
 * count or unequal length means the strings are not anagrams.
 *
 * Time: O(n).
 * Space: O(1), because the array always has 26 entries.
 */
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        array<int, 26> frequency{};

        for (char c : s) {
            ++frequency[c - 'a'];
        }

        for (char c : t) {
            if (--frequency[c - 'a'] < 0) {
                return false;
            }
        }

        return true;
    }
};
