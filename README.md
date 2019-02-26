# PythonAssertion

##Assertions
Assertions such as assert 1 == 2 are translated into 

''' if __debug__:
    	if not 1 == 2 : raise AssertionError #(optional_message)
'''

upon compile time. The debug message simply means it will not execute using the(optimize code) "-O" command line argument. Ex. 
> python -O assertion.py
This is both a blessing and a curse. It is a blessing because you can write test code that the user will not see. This is bad if you rely on that code being run and you accidentally turn assertions off. As such assertions should(unless for testing purposes) ever be used as a data validation tool.