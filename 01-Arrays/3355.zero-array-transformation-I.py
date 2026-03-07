"""
Problem : 3355. Zero array Transformation I
Platform: LeetCode
Difficulty: Medium

Approach: This problem contains m queries to handle on n size of data
 By using Brute force approach:
 we get order of m*n time complexity
 to reduce this we can use Difference array technique

 Difference Array method
 1. create a delta array by +1 and -1
 2. compute the prefix sum and name it no_computations_array
 3. compare no_computations_array and nums 

 TC = O(n)
 SC = O(n) for creating delta array
"""

nums = [4]
queries = [[0,0]]
n = len(nums)
def zero_array_transformation(nums,queries,n):
    delta_array = [0] * (n+1)
    for i in queries:
        delta_array[i[0]]+=1
        delta_array[i[1]+1]-=1

    total_count = [delta_array[0]]
    for i in range(len(delta_array)-1):
        total_count.append(total_count[i]+delta_array[i+1])

    for i,j in zip(total_count,nums):
        if i<j:
            return False
    return True

print(zero_array_transformation(nums,queries,n))