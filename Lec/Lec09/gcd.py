#python3 -m doctest -v ex.py
def gcd(m,n):
    """Returns the lagest k that divides both by m and n.
    k,m,n are all positive integers.

    >>> gcd(12,8)
    4
    >>> gcd(20,40)
    20
    """
    if m==n:
        return m
    elif m<n:
        return gcd(n,m)
    else:
        return gcd(m-n,n)