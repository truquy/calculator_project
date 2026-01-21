def add(a, b):
	return a+b

def subtract(a, b):
	return a-b

def multiply(a, b):
	return a*b

def divide(a, b):
	if b == 0:
		raise ValueError("Can not divide by rezo")
	return a/b

if __name__ == "__main__":
	print ("Simple calculator")
	print (f"5+3 = {add(5, 3)}")
	print (f"5-3 = {subtract(5, 3)}")
	print (f"5*3 = {multiply(5, 3)}")
	print (f"10/2 = {divide(10, 2)}")



