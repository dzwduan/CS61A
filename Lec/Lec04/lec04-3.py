"""Generalization."""

# python -m doctest -v .\lec04-3.py
# 如何提升抽象能力？

def sum_naturals(n):
    """Sum the first N natural numbers

    >>> sum_naturals(5)
    15
    """

    total,k = 0,1
    while k<=n:
        total,k = total+k,k+1
    return total


def sum_cube(n):
    """Sum the first N cubes of natutal numbers
    
    >>> sum_cube(5)
    225
    """
    total,k=0, 1
    while k<=n:
        total,k = total+pow(k,3),k+1
    return total
    