
DEFAULT_ON = True

def precondition(preconditions, *args, **kwargs):
	preconditions(args,kwargs)

def preCond(inval):
	if(numToGrow not in range(1,10)):
		raise Exception("string multiplier not within range(1,10")

@precondition(preCond)
def stringManipulator(strManip, numToGrow):
	strManip = strManip * numToGrow
	print(strManip)




def main():
	inp = input()
	while (inp != "q"):
		stringManipulator("stringOf", int(inp))
		inp = input()
	


if __name__ == '__main__':
	main()