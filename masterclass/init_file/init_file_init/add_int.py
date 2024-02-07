"""
Simple function to add two integers
"""

def add_int (a: int, b: int) -> int:
    assert (type(a) == int and type(b) == int)
    
    return a + b