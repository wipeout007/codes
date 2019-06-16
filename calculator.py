def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	a/b

a=int(input("Enter the first value  :  "))
b=int(input("Enter the second value :  "))
while(1):
	print("\n\n>>>>>>>>>>>>MENU<<<<<<<<<<<<\n")
	print("1. Add the numbers\n")
	print("2. Subtract the numbers\n")
	print("3. Multiply the numbers\n")
	print("4. divide the numbers\n")
	print("\n\n\n\n Enter your chooice  :  ")
	ch=input()
	if(ch=="1"):
		res=add(a,b)
		print("\n The result of naddition is   :   ", res)
	elif(ch=="2"):
		print("\n The result of subtraction is  :    ", sub(a,b))
	elif(ch=="3"):
		print("\n The result of mulitplication is :  ", mul(a,b))
	elif(ch=="4"):
		print("\n The result of division is  :  ", div(a,b))
	else:
		print("\n plz select the valid choice")
