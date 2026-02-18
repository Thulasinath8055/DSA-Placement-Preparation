def sortedSquares(nums):
    start = 0
    for i in range(len(nums)):
        nums[start] = nums[i]*nums[i]
        start +=1
    nums.sort()
    return nums
