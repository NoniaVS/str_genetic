"""
It is a simple function to be called from jupyter
After ifname_function_noif is imported, a message appears of "Test passed!" which takes
place in ifname_function_noif.py file
"""

def ifname_test ():
    print("Import ifname_function_if")
    from ifname_function_if import add_int as add_int_if

    print("Perform test")
    a = 20
    b = -2
    check = 18
    result = add_int_if(a, b)
    assert (abs(result - check) < 1e-8)

    print(f"Result file ifname_function_if.py : {result}\n")

    print("Import ifname_function_noif")
    from ifname_function_noif import add_int as add_int_noif

    print("Perform test")
    a = 20
    b = -2
    check = 18
    result = add_int_if(a, b)
    assert (abs(result - check) < 1e-8)

    print(f"Result file ifname_function_noif.py : {result}\n")
    
if __name__ == "__main__":
    ifname_test()