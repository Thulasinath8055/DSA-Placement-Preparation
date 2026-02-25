"""
problem: Majority element
platform: leetcode
difficulty: easy

Approach:
1. create num_count using counter
2. for key, count in nums_count.items()
3. if count is greater than or equal to int(len(nums)/2)+1
    return key
    
TC = O(n)
SC = O(n)

Approach 2:
To learn Boyer–Moore Voting Algorithm to make it 
SC = O(1) and TC = O(n)

"""

from collections import Counter

nums = [3,3,4]


def majority_ele(nums):
    nums_count = Counter(nums)
    for key, count in nums_count.items():
        if count >= int(len(nums)/2)+1:
            return key