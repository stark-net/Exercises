def multiplicatoin(x,y):
	print('\n\t',x * y,'\n')
def division(x,y):
	print('\n\t',x / y,'\n')
def addition(x,y):
	print('\n\t',x + y,'\n')
def substraction(x,y):
	print('\n\t',x - y,'\n')
x = int(input("Enter your 1st NUM: "))
OPERAND = input("/ for division\n* for times\n+ for sum\n- for mines\nEnter your choice: ")
y = int(input("Enter your 2nd NUM: "))
if(OPERAND == '*'):
	multiplicatoin(x,y)
elif(OPERAND == '/'):
	division(x,y)
elif(OPERAND == '+'):
	addition(x,y)
elif(OPERAND == '-'):
	substraction(x,y)
else:
	print("\n\tYour inputs which you Entered, aren't valid\n")
