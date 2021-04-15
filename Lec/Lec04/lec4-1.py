"""Gereralization."""
from math import pi,sqrt

#这样写违背了no repeat原则

def area(r):
    assert r>0, 'A length must be positive'
    return r*r

def area_circle(r):
    assert r>0, 'A length must be positive'
    return r*r*pi

def area_hexagon(r):
    assert r>0, 'A length must be positive'
    return r*r*3*sqrt(3)/2


