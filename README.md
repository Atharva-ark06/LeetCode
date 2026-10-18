# LeetCode Solutions

A collection of LeetCode solutions organized by problem number and title. The repository focuses on readable implementations, efficient algorithms, and concise notes about the approach and complexity.

## Solutions

| Problem | Title | Main technique | Time | Extra space |
|---:|---|---|---:|---:|
| 3 | Longest Substring Without Repeating Characters | Sliding window + last-seen indices | O(n) | O(min(n, charset)) |
| 26 | Remove Duplicates from Sorted Array | Two pointers | O(n) | O(1) |
| 49 | Group Anagrams | Character-frequency hashing | O(n × k) | O(n × k) |
| 53 | Maximum Subarray | Kadane's algorithm | O(n) | O(1) |
| 136 | Single Number | Bitwise XOR | O(n) | O(1) |
| 141 | Linked List Cycle | Floyd's cycle detection | O(n) | O(1) |
| 167 | Two Sum II – Input Array Is Sorted | Two pointers | O(n) | O(1) |
| 169 | Majority Element | Boyer–Moore voting | O(n) | O(1) |
| 206 | Reverse Linked List | Iterative pointer reversal | O(n) | O(1) |
| 283 | Move Zeroes | Two pointers | O(n) | O(1) |
| 3005 | Count Elements With Maximum Frequency | Frequency counting | O(n) | O(u) |
| 344 | Reverse String | Two pointers | O(n) | O(1) |
| 387 | First Unique Character in a String | Frequency counting | O(n) | O(1) for lowercase English letters |
| 392 | Is Subsequence | Two pointers | O(n) | O(1) |

> Complexity notes are approximate and depend on input length and constraints. Here, n is the input size, k is the maximum word length, and u is the number of distinct values.

## Repository conventions

- Each solution is stored in its own file named with the LeetCode problem number and title.
- Prefer clear, efficient approaches and include time and space complexity where useful.
- Some files are written in the language indicated by their extension; check each file before running it.
- Linked-list problems use the `ListNode` definition provided by LeetCode unless a local definition is explicitly included.

## Running Python examples

For Python files that include assertion examples, run the file with Python 3:

```bash
python "3. Longest Substring Without Repeating Characters.py"
python "49. Group Anagrams.py"
python "53. Maximum Subarray.py"
```

These examples are lightweight sanity checks, not a substitute for running the full test cases on LeetCode.

## Goals

This repository supports consistent algorithm practice, stronger data-structure fundamentals, and maintainable solution code.
