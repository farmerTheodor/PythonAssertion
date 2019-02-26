# PythonAssertion

##Assertions
Assertions such as assert 1 == 2 are translated into 

''' if __debug__:
    if not 1 == 2 : raise AssertionError #(optional_message)
'''

upon compile time. The debug message simply means it will not execute using the(optimize code) "-O" command line argument. Ex. 
> python -O assertion.py
