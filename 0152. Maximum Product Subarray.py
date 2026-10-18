class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maximum = minimum = answer = nums[0]
        for num in nums[1:]:
            if num < 0:
                maximum, minimum = minimum, maximum
            maximum = max(num, maximum * num)
            minimum = min(num, minimum * num)
            answer = max(answer, maximum)
        return answer
