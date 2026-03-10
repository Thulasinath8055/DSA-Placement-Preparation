"""
Problem: 35. search insert position
Platform: Leetcode
Difficulty: easy

Approach:
Binary search approach with performing checks on nums[mid]

TC = O(log(n))
SC = O(1)
"""

def searchInsert(nums, target) :
    left = 0
    right = len(nums) - 1

    while(left<=right):
        mid = (left + right) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    if nums[mid] < target:
        return mid+1
    else: 
        return mid