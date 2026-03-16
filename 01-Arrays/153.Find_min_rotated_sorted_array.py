"""
Problem: 153. Find minimum in rotated sorted array
Platform: Leetcode
Difficulty: Medium

Approach:
find the index of pivot and retun pivot element
To find pivot
use binary search modified where
if nums[mid] < nums[mid-1]:
    return mid #pivot index
else:
    follow binary search pattern for left and right
"""

nums = [11,13,15,17]
#7,8,9,1,2

def pivot_index(nums):
    if len(nums) == 0:
        return 0
    left,right = 0,len(nums)-1
    while left<=right:
        mid = (left+right)//2
        if nums[mid]<nums[mid-1] and mid>0:
            return mid
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid-1
    return 0
x = pivot_index(nums)
print(nums[x])
