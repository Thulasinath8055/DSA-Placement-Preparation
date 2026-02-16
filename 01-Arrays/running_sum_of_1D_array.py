"""
Problem: Running sum of 1D array - 1480
Platform: Leetcode
Difficulty: Easy

Approach-1: Brute force approach 

1. create an output array
2. for each index value in nums
3. slice continuously and calculate sum of the sliced part of that array
4. append every calculated sum into the output array
5. return the output array

Time complexity: O(N^2)
Space complexity: O(N)

Approach-2: 
1. iterate from the second element of the given array (nums)
2. make the current element sum of previous value and current value
3. return the array

Time complexity: O(N)
Space complexity: O(1)

"""
nums = [1,1,1,1]
for i in range(len(nums)-1):
    nums[i+1] = nums[i+1] + nums[i]
print(nums)