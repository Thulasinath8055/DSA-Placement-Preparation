"""
Problem: Two sum - 1
Platform: Leetcode
Difficulty: Easy

Approach:
- Use hashmap
- Store value -> index
- check complement
- return complement and index if found else
- return empty list

Time: O(n)
Space: O(n)

"""

def twoSum(nums, target):
    # innitialize a dict for storing num to index
    mp = {}
    
    for i, num in enumerate(nums):
        # compute diff for each num in nums
        diff = target - num
        
        if diff in mp:
            return [mp[diff], i]
        
        # map every non complement = target value in dict with num to its index
        mp[num] = i
        