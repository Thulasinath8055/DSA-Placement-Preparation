
"""
Problem: Range_sum_query - 303
Platform: Leetcode
Difficulty: easy

Approach: Prefix sum concept
1. Use prefix sum concept
2. calulate prefix sum to avoid redundant calculation of sum range
3. sum value till right - sum value till left-1 will give us the sum range(left, right)

TC = O(n)
SC = O(n)
"""
class NumArray:

    def __init__(self, nums):
        self.prefix_sum = [0]
        # calculation of prefix sum array
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        # calculation of sum range using prefix array
        return self.prefix_sum[right+1] - self.prefix_sum[left]

nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)

print(numArray.sumRange(0, 2))  # Output: 1
print(numArray.sumRange(2, 5))  # Output: -1
print(numArray.sumRange(0, 5))  # Output: -3