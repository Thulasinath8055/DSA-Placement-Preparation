"""
Problem: Search in rotated sorted array
Platform: Leetcode
Difficulty: Medium

Approach:
First
find the pivot index
    if the mid value is less than its prev value
        i.e pivot index
    else
    bin search conditions for left and right

Second
Decide which half to search for the target the first half till k or the second half.

TC = O(log(n))
SC = O(1)
"""

nums = [4]
target = 2

def find_pivot_index(nums):
    if len(nums)==1:
        return 0
    left = 0
    right = len(nums)-1
    while(left<=right):
        mid = (left+right)//2
        #minimum condition
        if nums[mid] < nums[mid-1] and mid > 0:
            return mid
        if nums[mid]>nums[right]:
            left = mid+1
        else:
            right = mid-1
    return 0
def bin_search(left,right,nums,target):
    while(left<=right):
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1
k = find_pivot_index(nums)
if target >= nums[k] and target <= nums[len(nums)-1]:
    print(bin_search(left = k, right = len(nums)-1,nums = nums,target = target))
else:
    print(bin_search(left = 0,right = k-1, nums = nums, target = target))
