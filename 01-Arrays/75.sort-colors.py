#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# --- THE THREE-COLOR PARTITIONING (DUTCH NATIONAL FLAG) LOGIC ---
# Using two fences (low, high) to sort three values (0, 1, 2) in one pass:
# 
# 1. If mid is 0 (Red): Swap nums[mid] with nums[low]. 
#    Move both 'low' and 'mid' forward because the new value at mid is guaranteed sorted.
# 
# 2. If mid is 1 (White): No swap needed.
#    Simply move 'mid' forward to the next element.
# 
# 3. If mid is 2 (Blue): Swap nums[mid] with nums[high]. 
#    Decrease 'high' fence, but DO NOT move 'mid' forward, 
#    as the newly swapped element at mid has not been reviewed yet.

# TC = O(N)
# SC = O(1)
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low , mid = 0,0
        high = len(nums) - 1
        while(mid<high):
            if nums[mid]==0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
        
# @lc code=end

