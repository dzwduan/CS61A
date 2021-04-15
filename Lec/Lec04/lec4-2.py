"""Gereralization."""
from math import pi,sqrt

#改进
def area(r,shape_constant):
    assert r>0, 'A length must be positive'
    return r*r*shape_constant

def area(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)

def area_hexagon(r):
    return area(r,3*sqrt(3)/2)

