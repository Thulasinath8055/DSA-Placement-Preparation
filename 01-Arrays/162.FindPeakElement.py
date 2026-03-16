"""
Problem : Find peak elemt
Platform: Leetcode
Difficulty: Medium

Intution: Visualize the array as a sequence of hills and valleys—there's always at least one peak
because adjacent elements differ and edges are -∞. Instead of checking every neighbor (O(n)), 
ask: "Can I discard half the array confidently?" 
Compare the middle to its right neighbor: if rising, a peak exists rightward (slope guarantees it);
if falling, a peak is leftward (or mid). 
This halves the search space every step, like standard binary search but on trends, not targets.

TC = O(log(N))
SC = O(1)
"""
nums = [1,2,3,1]

def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    while left<right:
        mid = (left+right)//2
        if nums[mid]<nums[mid+1]:
            left = mid+1
        else:
            high = mid
    return high
print(findPeakElement(nums))
