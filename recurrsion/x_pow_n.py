"""
50. Pow(x, n)
Platform: Leetcode
Difficulty: Medium

Approach:
base cases 0 and 1 
If positive - think about even and odd n values - try to find the pattern
if negative - return 1/positive value

TC - O(log(n))
SC - O(1)
"""

def x_pow_n(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n>0:
        if n%2==0:
            z1 = x_pow_n(x,n/2)
            return z1*z1
        else:
            z2 = x_pow_n(x,int(n/2))
            return z2 * z2 * x
    else:
        return minus(x,n)
def minus(x,n):
    return 1/(x_pow_n(x,-n))
print(x_pow_n(2.1000,3))