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
s = 'abbba'
k = 1
count = {}
max_freq = 0
left = 0
result = 0

for i in range(len(s)):
    count[s[i]] =  count.get(s[i],0) + 1
    max_freq = max(max_freq,count[s[i]])
    while (i-left+1) - max_freq > k:
        count[s[left]]-=1
        left +=1
    result = max(result, i-left+1)
print(result)