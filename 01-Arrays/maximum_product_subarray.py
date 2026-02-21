"""
Problem : maximum product subarray 152
Platform: Leetcode

Approach:
1. initialize maximum and minimum product value with 1
2. initialize result with first num
3. iterate through the array
4. we need three comparision for each ele (num, num*max_prod, num*min_prod)
5. calculate max_prod and min_prod
6. calculate result which is max(result, max_prod)
7. return result

TC = O(N)
SC = O(1)
"""
nums = [-2,-3,-1,-1]

max_prod = 1
min_prod = 1
result = nums[0]

for num in nums:
    candidates = (num, num*max_prod, num*min_prod)
    max_prod, min_prod = max(candidates), min(candidates)
    result = max(result, max_prod)
print(result)
