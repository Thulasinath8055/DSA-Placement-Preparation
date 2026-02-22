Summary
1. Prefix sum concept
    Prefix sum concept in arrays are useful whenever we want to calculate sumrange 
    we have to calculate every time for each sumrange 
    which is inefficient so we need another array to store the prefix sum of the current array 

2. Two pointer 
    Two pointer approach can be used when we need two vars to track different speed, different sides of the array 

    it can be used using for loop and while loop also

3. Sliding window 
    When we need to solve problems that involve subarrys or window
    it can be two types fixed and dynamic
    window -> compute -> slide -> one by one 

    How to identify
        Finding max/mim subarray, substring which satisy specific condition 

4. Kadane's Algorithm
    (+ve) + (++ve) = +
    (-ve) + (++ve) = +
    *(+ve) + (--ve) = -*
    two vars curr_sum = 0 and max_sum = 0

    calculate curr_sum and max_sum for each ele
    if curr_sum<0
        set cur_sum = 0

