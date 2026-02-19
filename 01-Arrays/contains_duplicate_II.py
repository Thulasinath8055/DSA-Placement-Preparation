"""
Problem: contains duplicate II - 219
Platform: Leetcode
Difficulty: easy

Approach: Sliding window (static)
1. initialize a set (window) to track the minimum distance k
2. iterate through the array and if element is found in set return True
3. if not found add it the set
4. if the size of the increases the limit k remove the oldest found value.

Lesson : in sliding window , window can be another tracked using another data structure other than the given list.

TC = O(n)
SC = O(1)

"""

nums = [1,3,4,1,0]
k = 3
def contains_duplicate_II(nums, k):
    x = set()
    for i in range(len(nums)):
        #if ele found in set return true
        if nums[i] in x:
            return True
        # if not found add it to set
        x.add(nums[i])
        if len(x) > k:
            x.remove(nums[i])
    return False
print(contains_duplicate_II())
    