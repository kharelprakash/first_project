def calculate():
	operation =input('''
Please choose your operator:
+ for addition
- for substraction
* for multiplication
/ for division
''')
	num1=int(input('Enter the first number:'))
	num2=int(input('Enter the second number:'))
	if operation == '+':
		print(num1+num2)
	elif operation == '-':
		print(num1-num2)
	elif operation == '*':
		print(num1*num2)
	elif operation == '/':
		print(num1/num2)
	else:
		print('Wrong input choice')
def again():
	calc_again = input('''
Do you want to calculate again?
Please type Y for Yes And N for NO.
''')
	if calc_again.upper() =='Y':
		calculate()
	elif calc_again.upper() == 'N':
		print('See You Again.')
	else:
		again()
calculate()

