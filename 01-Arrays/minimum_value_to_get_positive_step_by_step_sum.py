"""
Problem: minimum-value-to-get-positive-step-by-step-sum
Platform: Leetcode
Difficluty: easy

Approach:
Use prefix sum array to track the minimum value to get positive step by step sum
get - min value in prefix sum array and add one to it
"""


nums = [1,2]              
def minimum_value_to_get_positive_step_by_step(nums):
    prefix_sum = [0]
    for i in range(len(nums)):
        prefix_sum.append(nums[i]+prefix_sum[i])
    return prefix_sum
print(minimum_value_to_get_positive_step_by_step(nums))
print((-(min(minimum_value_to_get_positive_step_by_step(nums))))+1)