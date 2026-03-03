#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
"""
Approach:
1. Sort the Array: Essential to make pointer movement predictable and duplicates easy to spot.

2. Fix One, Search Two: Use a for loop to fix nums[i] and treat the rest of the array as a Two-Sum problem.

3. Two-Pointer Setup: Initialize l = i + 1 and r = last index, searching while l < r.

4. Steer the Sum: If the sum is < 0, move l right to increase value; if > 0, move r left to decrease it.

5. Record & Shrink: When the sum is 0, save the triplet and move both pointers inward.

6. Skip Duplicates: Use while loops to "fast-forward" i, l, and r past identical values to avoid redundant results.

TC = O(N2)
SC = O(1)
"""
# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        for i in range(len(nums)):
        # 1. Stop if the pivot is positive (no more triplets possible)
            if nums[i] > 0:
                break
            
            # 2. Skip duplicates for the pivot 'i'
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 3. Two-Pointer Search
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s < 0:
                    l += 1 # Need a bigger sum
                elif s > 0:
                    r -= 1 # Need a smaller sum
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    
                    # 4. Skip duplicates for l and r to avoid same triplet
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    # Move both after finding a match
                    l += 1
                    r -= 1

        return output
# @lc code=end

