
# nums = [-2,0,-1]
# def maxProduct(nums):
#     curr_max = nums[0]
#     curr_min = nums[0]
#     result = nums[0]

#     for i in range(1, len(nums)):
#         num = nums[i]

#         if num < 0:
#             curr_max, curr_min = curr_min, curr_max

#         curr_max = max(num, curr_max * num)
#         curr_min = min(num, curr_min * num)

#         result = max(result, curr_max)

#     return result
# print(maxProduct(nums))