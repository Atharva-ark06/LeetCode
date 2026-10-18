# LeetCode Solutions

A collection of LeetCode solutions organized by problem number and title. The repository focuses on readable implementations, efficient algorithms, and concise notes about approach and complexity.

## Solutions

| Problem | Title | Main technique | Time | Extra space |
|---:|---|---|---:|---:|
| 1 | Two Sum | Hash map | O(n) | O(n) |
| 2 | Add Two Numbers | Linked-list traversal | O(max(m, n)) | O(1) |
| 3 | Longest Substring Without Repeating Characters | Sliding window | O(n) | O(k) |
| 9 | Palindrome Number | Numeric reversal | O(log n) | O(1) |
| 13 | Roman to Integer | Greedy scan | O(n) | O(1) |
| 20 | Valid Parentheses | Stack | O(n) | O(n) |
| 21 | Merge Two Sorted Lists | Two pointers | O(m+n) | O(1) |
| 26 | Remove Duplicates from Sorted Array | Two pointers | O(n) | O(1) |
| 35 | Search Insert Position | Binary search | O(log n) | O(1) |
| 36 | Valid Sudoku | Constraint checking | O(1) for 9x9 | O(1) |
| 49 | Group Anagrams | Frequency hashing | O(n × k) | O(n × k) |
| 53 | Maximum Subarray | Kadane's algorithm | O(n) | O(1) |
| 70 | Climbing Stairs | Dynamic programming | O(n) | O(1) |
| 88 | Merge Sorted Array | Two pointers from end | O(m+n) | O(1) |
| 94 | Binary Tree Inorder Traversal | Tree traversal | O(n) | O(h) |
| 104 | Maximum Depth of Binary Tree | DFS | O(n) | O(h) |
| 118 | Pascal's Triangle | Dynamic programming | O(r²) | O(r²) |
| 121 | Best Time to Buy and Sell Stock | One-pass minimum | O(n) | O(1) |
| 122 | Best Time to Buy and Sell Stock II | Greedy | O(n) | O(1) |
| 125 | Valid Palindrome | Two pointers | O(n) | O(1) |
| 136 | Single Number | Bitwise XOR | O(n) | O(1) |
| 141 | Linked List Cycle | Floyd's cycle detection | O(n) | O(1) |
| 155 | Min Stack | Stack with running minimum | O(1) per operation | O(n) |
| 167 | Two Sum II – Input Array Is Sorted | Two pointers | O(n) | O(1) |
| 169 | Majority Element | Boyer–Moore voting | O(n) | O(1) |
| 198 | House Robber | Dynamic programming | O(n) | O(1) |
| 202 | Happy Number | Cycle detection | O(log n) per step | O(log n) |
| 203 | Remove Linked List Elements | Sentinel node | O(n) | O(1) |
| 205 | Isomorphic Strings | Bidirectional mapping | O(n) | O(k) |
| 206 | Reverse Linked List | Iterative pointer reversal | O(n) | O(1) |
| 217 | Contains Duplicate | Hash set | O(n) | O(n) |
| 219 | Contains Duplicate II | Index map | O(n) | O(n) |
| 226 | Invert Binary Tree | DFS | O(n) | O(h) |
| 238 | Product of Array Except Self | Prefix/suffix products | O(n) | O(1) extra |
| 242 | Valid Anagram | Character counts | O(n) | O(1) for fixed alphabet |
| 268 | Missing Number | Arithmetic sum | O(n) | O(1) |
| 283 | Move Zeroes | Two pointers | O(n) | O(1) |
| 3005 | Count Elements With Maximum Frequency | Frequency counting | O(n) | O(u) |
| 303 | Range Sum Query – Immutable | Prefix sums | O(n) build, O(1) query | O(n) |
| 344 | Reverse String | Two pointers | O(n) | O(1) |
| 347 | Top K Frequent Elements | Frequency buckets | O(n) | O(n) |
| 387 | First Unique Character in a String | Frequency counting | O(n) | O(1) for lowercase English letters |
| 392 | Is Subsequence | Two pointers | O(n) | O(1) |
| 409 | Longest Palindrome | Character counts | O(n) | O(k) |
| 496 | Next Greater Element I | Monotonic stack | O(n+m) | O(n) |
| 543 | Diameter of Binary Tree | Postorder DFS | O(n) | O(h) |
| 704 | Binary Search | Binary search | O(log n) | O(1) |
| 733 | Flood Fill | DFS | O(rows × cols) | O(rows × cols) worst case |
| 876 | Middle of the Linked List | Slow/fast pointers | O(n) | O(1) |
| 1480 | Running Sum of 1d Array | Prefix accumulation | O(n) | O(1) extra |

> Complexity notes are approximate and depend on input constraints. Here, n is input size, k is a maximum word length or distinct-character count as applicable, u is the number of distinct values, and h is tree height.

## Repository conventions

- Each solution is stored in its own file named with the LeetCode problem number and title.
- Prefer clear, efficient approaches and include time and space complexity where useful.
- Python files with assertion examples can be run directly with Python 3.
- Linked-list and tree problems include local node definitions where useful for standalone examples.

## Running Python examples

```bash
python "3. Longest Substring Without Repeating Characters.py"
python "49. Group Anagrams.py"
python "53. Maximum Subarray.py"
python "733. Flood Fill.py"
```

These examples are lightweight sanity checks, not a substitute for running full test cases on LeetCode.

## Goals

This repository supports consistent algorithm practice, stronger data-structure fundamentals, and maintainable solution code.
