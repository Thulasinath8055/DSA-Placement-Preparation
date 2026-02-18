"""
Problem: Move zeros - 283
Platform: Leetcode
Difficulty: easy

Approach: Two pointer
Initialize two pointers for read and write
one pointer read to read the data and anoter pointer to write the data back into the same list
1. set first posi as write
2. loop over the array using read
3. if we read non zero 
        swap with write posi ele
        and move the write posi by one
4. return the nums array

TC = O(n)
SC = O(1)
"""
nums = [0,1,0,3,12]

# write pointer
write = 0
for read in range(len(nums)):
    if nums[read]!=0:
        nums[read],nums[write] = nums[write],nums[read]
        write+=1

print(nums)