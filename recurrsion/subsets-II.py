nums = [1,2,2]
result = []
def backtrack(start,curr_subset):
    result.append(curr_subset.copy())

    for i in range(start,len(nums)):
        if i > start and nums[i] == nums[i-1]:
            continue
        curr_subset.append(nums[i])
        backtrack(i+1,curr_subset)
        curr_subset.pop()
backtrack(0,[])
print(result)