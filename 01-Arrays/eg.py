# nums = [[1,2,3],[10],[40]]
# global_sum = 0
# for i_i in nums:
#     curr_sum = 0
#     for i in i_i:
#         curr_sum+=i
#     global_sum = max(curr_sum, global_sum)
# print(global_sum)

height = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(height) - 1
area = 0
while left < right:
    width = right - left
    length = min(height[left],height[right])
    area = max(area, (width * length))
    if height[left]<= height[right]:
        left+=1
    else:
        right-=1
print(area)