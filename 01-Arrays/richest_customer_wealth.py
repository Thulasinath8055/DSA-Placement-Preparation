"""
Problem: Richest customer wealth - 1672
Platform: Leetcode
Difficulty: Easy

Approach:
1. set a variable for setting the max_wealth calculated so far
2. for every nested list calculate sum and set max(calculated and max_wealth)
3. return the max_wealth

Time complexity: O(M*N)
Space Complexity: O(1)
"""
accounts = [[1,0],[5,6]]
x = 0
for i in range(len(accounts)):
    x = max(x, sum(accounts[i]))
print(x)