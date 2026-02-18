nums = [-4,-1,0,3,10]
end = len(nums)-1
i = 0
while i<=end:
    if ((nums[i]*nums[i]) > (nums[end]*nums[end])):
        nums[i],nums[end] = nums[end]*nums[end],nums[i]*nums[i]
        i+=1
        end-=1
    else:
        nums[i] = nums[i] * nums[i]
        nums[end] = nums[end] * nums[end]
        i+=1
        end-=1
print(nums)