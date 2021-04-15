from operator import floordiv, mod 

#python -m doctest -v .\lec2.py  测试
#python -i lec2.py  交互

def divide_exact(n,d=10):
    """
    return quotient and remainder of dividing N by D.

    >>> q,r = divide_exact(2012,10)
    >>> q
    201
    >>> r
    2
    """
    return floordiv(n,d),mod(n,d)