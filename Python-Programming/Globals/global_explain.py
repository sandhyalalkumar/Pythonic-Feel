thisvar = 1

def function1():
	global thisvar
	print thisvar
	thisvar = thisvar + 1
	print thisvar

if __name__ == '__main__':

	function1()

