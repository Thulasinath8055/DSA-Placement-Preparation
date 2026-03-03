#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
"""
Approach: 
1. Using two pointer approach
2. set two pointers starting and ending
3. calculate area which is (width = distance of start and end) * (length = min(l1 and l2))
4. moving shortest among two lines as width decreases and moving longest make only negative impact on area
5. repeat this untill both of them meet

TC = O(N)
SC = O(1)
"""
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            width = right - left
            length = min(height[left],height[right])
            area = max(area, (width * length))
            if height[left]<= height[right]:
                left+=1
            else:
                right-=1
        return area
        
# @lc code=end

