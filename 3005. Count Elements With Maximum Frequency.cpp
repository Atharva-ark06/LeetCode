#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> freq;  // count frequencies
        int maxFreq = 0;

        // count frequencies and track max frequency
        for (int num : nums) {
            freq[num]++;
            maxFreq = max(maxFreq, freq[num]);
        }

        int total = 0;
        // sum occurrences of elements with max frequency
        // Use entry.second instead of structured bindings for C++14 compatibility.
        for (const auto& entry : freq) {
            if (entry.second == maxFreq) {
                total += entry.second;
            }
        }
        return total;
    }
};