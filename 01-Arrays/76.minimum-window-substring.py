#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Frequency map of characters we need from t
        target_map = {}
        for char in t:
            target_map[char] = target_map.get(char, 0) + 1

        # Number of unique characters in t that must be fully satisfied
        required = len(target_map)
        
        # window_map tracks the characters in our current sliding window
        window_map = {}
        
        # formed tracks how many unique characters have met their target frequency
        formed = 0
        
        # ans stores (window_length, left_index, right_index)
        ans = float("inf"), None, None
        
        left = 0
        for right in range(len(s)):
            # 1. Expand: Add character from the right to the window
            char = s[right]
            window_map[char] = window_map.get(char, 0) + 1

            # If the character's frequency matches the target, we've satisfied one unique char
            if char in target_map and window_map[char] == target_map[char]:
                formed += 1

            # 2. Contract: Try to shrink the window while it remains valid (Exhale)
            while left <= right and formed == required:
                char_left = s[left]

                # Save the smallest window found so far
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # 3. Move the left pointer forward and update the window state
                window_map[char_left] -= 1
                if char_left in target_map and window_map[char_left] < target_map[char_left]:
                    formed -= 1
                
                left += 1    

        # If no window was found, ans[0] remains infinity
        if ans[0] == float("inf"):
            return ""
        
        # Return the substring using the recorded indices
        return s[ans[1] : ans[2] + 1]
# @lc code=end

