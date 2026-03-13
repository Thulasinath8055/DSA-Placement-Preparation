"""
34. First and last position of elemtnt in a sorted array

Key idea : 
one 'Bound' Variable is required to trace left and right two times 
even after finding the target position
"""


nums = [1,2,3,3,3,3,3,3,4]
target = 3

def findBound(isFirst):
    left,right = 0,len(nums)-1
    bound = -1
    while(left<=right):
        mid = (left+right)//2
        if nums[mid] == target:
            bound = mid
            if isFirst:
                right = mid-1
            else:
                left = mid+1
        elif nums[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return bound
print(findBound(True),findBound(False))
