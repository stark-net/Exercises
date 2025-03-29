def fact(a):
	if(a == 1):
		return 1
	else:
		return fact(a) * fact(a - 1)

a = int(input("Enter a number to I calculate the Factoriel of it:  "))

re = fact(a)
print(re)
