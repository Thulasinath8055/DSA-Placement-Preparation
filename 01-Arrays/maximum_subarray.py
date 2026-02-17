"""
Problem: Maximum subarray - 53
Platform: Leetcode
Difficulty: Medium

Approach:
1. create two variable for tracking current sum and maximum sum
2. curr_sum = 0 and max_sum = -ve infinity (float('-inf') in python)
3. iterate over the array using a variable i
4. calculate current sum for each element curr_sum += nums[i]
5. calculate maximum sum by max(curr_sum, max_sum)
6. check if curr_sum<0
        yes set curr-sum = 0
7. return the max_sum

Time complexity: O(N)
Space complexity: O(1)
"""

def maxSubArray(self, nums):
    #Using Kadanes Algorithm
    curr_sum = 0 
    max_sum = float('-inf')
    for i in range(len(nums)):
        curr_sum+= nums[i]
        max_sum = max(curr_sum, max_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum