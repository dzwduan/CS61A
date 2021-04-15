"""Generalization."""

def make_adder(n):
    """return a function that takes one argument k 
    and reutrn k+n
    
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k+n
    return adder

#这里把make_addr(1)整体看作一个函数adder
make_adder(1)(2)

"""
1.函数既能作为参数也能作为返回值
"""