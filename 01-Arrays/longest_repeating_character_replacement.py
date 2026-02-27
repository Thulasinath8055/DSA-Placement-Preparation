"""
Problem: 424. Longest repeating character replacement 
Platform: Leetcode
Difficulty: Medium

Approach:
1. Use a freqency dictionary
2. Expand right
3. Track the highest frequency char in window
4. If replacement needed in window > k -> shrink window
5. track max result
Time Complexity: O(n)
Space COmplexity: O(n)
"""