"""
Problem: best_time_to_buy_and_sell_stock - 121
Platform: Leetcode
Difficulty: Easy

Approach: Naive
1. create a max-profit variable and initialize it with 0
2. run two loops with variables i and j 
    1st loop from i to n (for buying price)
    2nd loop from i+1 to n (as we cannot sell before buying) (for selling price)
3. for every buying and selling pair calculate max-profit
4. return max-profit
TC = O(N^2)
SC = O(1)

Approach: Optimal
1. create a varible for storing min_price_so_far
2. create another variable for storing max_profit
3. loop over the array using a variable i
4. for every value track min_price_so_far and calculate max_profit
5. return max_profit

Time complexity: O(N)
Space Complexity: O(1)
"""

def naive_approach(nums):
    max_profit = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            max_profit = max( max_profit, nums[i]-nums[j])
    return max_profit

def optimised_approach(nums):
    min_price_so_far = nums[0]
    max_profit = 0
    for num in nums:
        if num < min_price_so_far:
            min_price_so_far = num
        max_profit = max(max_profit, num-min_price_so_far)
    return max_profit
