
from ucb import trace
@trace
def count_patitions(n,m):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    else:
        with_m = count_patitions(n-m,m)
        without_m = count_patitions(n,m-1)
        return without_m+without_m

num = count_patitions(5,3)
print(num) 