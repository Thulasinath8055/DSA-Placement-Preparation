"""
704. Binary Search

Approach:
Maintain two pointers left and right
Use while loop for left<=right
three cases: 1. if mid_val == target -> return target
             2. if mid_val < target -> move left ptr mid + 1
             3. else -> mid_val > target -> move right ptr mid - 1
"""

def search(nums, target):
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = int((left+right)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1