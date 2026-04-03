def subsets(self, nums):
    result = []
    def backtrack(start,curr_subset):
        result.append(curr_subset.copy())

        for i in range(start,len(nums)):
            curr_subset.append(nums[i])
            backtrack(i+1,curr_subset)
            curr_subset.pop()
    backtrack(0,[])
    return result