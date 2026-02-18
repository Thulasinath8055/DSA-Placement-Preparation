"""
Problem: remove duplicate from sorted array - 26
Platform: Leetcode
Difficulty: easy

Approach: Two pointer approach
1. use one variable to track first unique element identified so far (intially set it with first ele of given array)
2. use two pointers slow and fast (set slow ptr to 0)
3. loop over the array using fast ptr 
4. if fast ptr ele is not equal to FUE
    update FUE with fast ptr ele
    move slow by one step
    update slow ele with fue
5. after the loop, set all elements after slow ptr to _
6. return the slow+1 value it is the number of Unique elements found

Learned about how to modify arrays or lists inplace using two pointer approach

TC = O(n)
SC = O(1)
"""

nums = [1,1,1,1,3,3]
# variable for tracking first unique element found
fue = nums[0]
# variable or ptr to write the found fue value
slow = 0
# fast variable to read or to find the fue value in the array
for fast in range(len(nums)):
    # if ele of fast ptr is not equal to fue
    if nums[fast]!=fue:
        fue = nums[fast] #update fue
        slow +=1 #move write var 
        nums[slow] = fue #write the found fue
nums[slow+1:] = ['_'] * len(nums[slow+1:]) #replace all elements after slow varible to "_"
print(slow+1) #prints number of une in the array
print(nums)