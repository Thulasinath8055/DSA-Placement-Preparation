# nums = [[1,2,3],[10],[40]]
# global_sum = 0
# for i_i in nums:
#     curr_sum = 0
#     for i in i_i:
#         curr_sum+=i
#     global_sum = max(curr_sum, global_sum)
# print(global_sum)

nums = [7,6,4,3,1]
gm = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[j] - nums[i] > gm:
            gm = nums[j] - nums[i]
print(gm)   