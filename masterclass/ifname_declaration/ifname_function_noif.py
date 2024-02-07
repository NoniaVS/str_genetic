"""
I define a simple addition function to add two integers.
In this function, I do not declare the if __name__ == "__main__": statement.
"""

def add_int (a: int, b: int) -> int:
    assert (type(a) == int and type(b) == int)
    
    return a + b


# Secure testing declaration
n1 = 2
n2 = 3
res_test = 5
result = add_int(n1, n2)

assert (abs(result - res_test) < 1e-8)

print("Test passed!")