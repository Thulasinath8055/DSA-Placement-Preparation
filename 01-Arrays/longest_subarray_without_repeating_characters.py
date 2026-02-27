"""
Problem: Longest subarray without repeating character
Platform: Leetcode
Difficulty: Medium

Approach:
1. Move right pointer
2. add every unique ele to set
3. if duplicate found (use while loop till dup is gone and every time remove left while moving left)
4. move left pointer till duplicate gone
5. keep track of maximum length

Time Complexity: O(n)
Space COmplexity: O(n)
"""
s = 'abcabcbb'
track = set()
left = 0
max_len = 0

for right in range(len(s)):
    
    while s[right] in track:
        track.remove(s[left])
        left+=1
    track.add(s[right])
    max_len = max(max_len,right-left+1)
print(max_len)
    