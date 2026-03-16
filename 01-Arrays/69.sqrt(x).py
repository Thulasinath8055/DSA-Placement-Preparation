"""
Problem: Find Square root without using built in functions in O(log(n))
Platform: Leetcode
Difficulty: Easy

Approach: Mid * Mid square comparition is done with x
          Search space is halfed every time if mid square > x
          shift right to mid - 1
          Time complexity - O(log(n))
          Space complexity - O(1)
"""

def sqrt(x):
    left = 0
    right = x
    while(left<=right):
        mid = (left+right)//2
        if mid*mid > x:
            right = mid-1
        else:
            left = mid + 1
    return right