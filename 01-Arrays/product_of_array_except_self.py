"""
Problem: 238
Platform: Leetcode
Difficulty: Medium

Approach:
we have to find the result array where result[i] is product of all the nums except itself (nums[i])

1. initialize a result array
2. iterate through start to end of nums
3. append prefix to result for each index and calculate prefix product till each index of the array nums
4. iterate another loop from the end to start
5. multiply suffix product for each index in the array and calculate suffix product till each index of the array nums


another approach
1. think about what if we have zeros in the array
2. if no zeros?
3. if one zero?
4. if more than one zero?

TC = O(N)
SC = O(1) output array is not considered  

"""

nums = [-1,1,0,-3,3]
result = []
prefix = 1
suffix = 1

for i in range(len(nums)):
    result.append(prefix)
    prefix *= nums[i]

for i in range(len(nums)-1,-1,-1):
    result[i] *= suffix
    suffix *= nums[i]
    
print(result)
