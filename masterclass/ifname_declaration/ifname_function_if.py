"""
I define a simple addition function to add two integers.
In this function, for testing I declare the if __name__ == "__main__":
statement to ensure that it is not called outside this execution file.
"""

def add_int (a: int, b: int) -> int:
    assert (type(a) == int and type(b) == int)
    
    return a + b


# Secure testing declaration
if __name__ == "__main__":
    n1 = 2
    n2 = 3
    res_test = 5
    result = add_int(n1, n2)
    
    assert (abs(result - res_test) < 1e-8)
    
    print("Test passed!")