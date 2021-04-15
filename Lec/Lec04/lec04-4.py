"""Generalization."""

# python -m doctest -v .\lec04-3.py
# python -i lec04-4.py

from operator import mul

def identity(k):
    return k

def cube(k):
    return pow(k,3)

def pi_term(k):
    return 8/mul(4*k-3,4*k-1)

def summation(n,term):
    """Sum the first N terms of a sequence.
    >>> summation(5,cube)
    225
    """
    total,k = 0,1
    while k<=n:
        total,k = total + term(k),k+1
    return total

    
#############################################

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
    