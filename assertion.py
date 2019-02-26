def thisFunctionWillRun():
	#will always be true because it is a tuple of 1==2 and "this is always true"
	assert(1 == 2, "error this is always true")
	print("thisFunctionWillRun")

def thisFunctionWillNotRun():
	assert 1 == 2, "error this is always false"
	print("thisFunctionWillNotRun")


def assertionsAndArrays():
	num1 = [1,5,3,6,2,3]
	num2 = [1,5,3,6,2,3]
	assert num1 == num2, "error array 1"
	num2 = [1,5,3]
	assert 1 in num1, "error array 2"
	assert set(num2).issubset(num1), "error array 3"
	print("assertionsAndArrays")

def main():
	thisFunctionWillRun()
	assertionsAndArrays()
	try:
		thisFunctionWillNotRun()
	except AssertionError as e:
		print(e)
	thisFunctionWillNotRun()



if __name__ == '__main__':
	main()