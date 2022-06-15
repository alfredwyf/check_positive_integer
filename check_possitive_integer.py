number = input('Please input a possitive integer: ')
try:
	number = int(number)
	if number > 20:
		print('your input: ' + str(number) + ' > 20')
	if number > 10:
		print('your input: ' + str(number) + ' > 10')
	if number > 0:
		print('your input: ' + str(number) + ' > 0')
	if number < 0:
		print('your input: ' + str(number) + ' is negative')
except ValueError as e:
	print('your input is not an integer.')