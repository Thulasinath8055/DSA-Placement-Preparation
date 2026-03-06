"""
Problem: Find the losers of the circular game
Platform: Leetcode
Difficultu: Easy

Approach:
1. Circular pointer login for zero based index is : curr = (curr + i*k)%n i.e 3%5 = 3 and 8%5 = 3
2. Create n number of False valued array i.e not visited array
3. untill array is False i.e not visited[i]
4. Do this
        set curr to visited
        update curr value with circular logic
5. return all the values Which are False i.e not visited

TC = O(N)
SC = O(N)
"""

def circular_game_losers(n,k):
    visited = [False] * n
    curr = 0
    ptr = 1

    while not visited[curr]:
        visited[curr] = True

        curr = (curr+ptr*k) % n
        ptr+=1

    return ([i+1 for i in range(n) if not visited[i]])


