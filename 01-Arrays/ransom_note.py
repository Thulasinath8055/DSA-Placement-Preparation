"""
Problem: Ransom note
Platform: Leetcode
DIfficulty: Easy

Approach:
1. Use Counter to to count frequency of each letter in magazine
2. for each char in ransomNote
    if char is not present in magazine_counter or zero
        return False
    else
        magazine_counter-=1
"""
from collections import Counter
ransomNote = 'abc'
magazine = 'abcdefadfadf'
flag = True
magazine_counter = Counter(magazine)
for char in ransomNote:
    if magazine_counter[char]<=0:
        flag = False
    magazine_counter[char]-=1

print(flag)