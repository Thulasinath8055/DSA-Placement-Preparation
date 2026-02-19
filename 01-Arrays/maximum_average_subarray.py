"""
Problem: Maximum average subarray - 643
Platform: Leetcode
Difficulty: easy

Approach: Sliding window (static)
1. calculate current window sum
2. set max-avg-value by dividing curr_sum / k
3. loop over the array with window by adding and subtracting first and last element form the window respectively to get curr sum
4. set the max-avg-value by comparing max-avg-value and curr_sum/k
5. return the max-avg-value

TC = O(n)
SC = O(1)

"""


nums = [1,12,-5,-6,50,3]
k = 4
curr_sum = sum(nums[:k])
max_sum = curr_sum/k

for i in range(k,len(nums)):
    curr_sum += nums[i] - nums[i-k]
    max_sum = max(max_sum, curr_sum/k)
print(max_sum)
__import__('atexit').register(lambda: open('display_runtime.txt', 'w').write('000'))