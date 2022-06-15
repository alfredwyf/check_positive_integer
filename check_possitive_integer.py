number = input('Please input a possitive integer: ')

if (number.isnumeric()):
	number = int(number)
	if number > 20:
		print('your input: ' + str(number) + ' > 20')
	if number > 10:
		print('your input: ' + str(number) + ' > 10')
	if number > 0:
		print('your input: ' + str(number) + ' > 0')
else:
	print('your input is not an integer or it is negative')