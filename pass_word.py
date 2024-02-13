import random
import time

options = {
	'CHAR_COUNT': 0,
	'INCLUDE_NUM': False,
	'INCLUDE_SYMBOLS': False
}

alpha = ('a' ,'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']','.','<', '>', '?', '/', '|', '\\', ';', ':', ',', '~', '`', "'", '"')

def uInput():
	global options
	global alpha
	global nums
	global symbols

	# Accept the word count as user input
	while True:
		options['CHAR_COUNT'] = int(input('Enter the number of characters: '))
		if options['CHAR_COUNT'] >= 8:
			break
		else:
			print('TThis password length is weak, enter the number "8" or higher!\n')

	# Asking the user whether numbers should be included
	while True:
		options['INCLUDE_NUM'] = input('Should numbers be included? (y/n): ').lower()
		if options['INCLUDE_NUM'] == 'y' or options['INCLUDE_NUM'] == 'n':
			if options['INCLUDE_NUM'] == 'y':
				options['INCLUDE_NUM'] = True
			elif options['INCLUDE_NUM'] == 'n':
				options['INCLUDE_NUM'] = False
			break
		else:
			print('Either "y" or "n" should be entered!\n')

	# Asking the user whether symbols should be included
	while True:
		options['INCLUDE_SYMBOLS'] = input('Should symbols be included? (y/n): ').lower()
		if options['INCLUDE_SYMBOLS'] == 'y' or options['INCLUDE_SYMBOLS'] == 'n':
			if options['INCLUDE_SYMBOLS'] == 'y':
				options['INCLUDE_SYMBOLS'] = True
			elif options['INCLUDE_SYMBOLS'] == 'n':
				options['INCLUDE_SYMBOLS'] = False
			break
		else:
			print('Either "y" or "n" should be entered!\n')

	create()

def create():
	global options
	global alpha
	global nums
	global symbols

	order = [1]

	# Include numbers if opted for
	if options['INCLUDE_NUM'] == True:
		order.append(2)

	# Include symbols if opted for
	if options['INCLUDE_SYMBOLS'] == True:
		order.append(3)

	pass_word = ''
	for x in range(options['CHAR_COUNT']):
		choice = random.choice(order)
		
		if choice == 1:
			case = random.randint(1,2)
			if case == 1:
				char = random.choice(alpha).lower()
			elif case == 2:
				char = random.choice(alpha).upper()
			pass_word+=char
		elif choice == 2:
			if options['INCLUDE_NUM'] == True:
				pass_word+=str(random.choice(nums))
		elif choice == 3:
			if options['INCLUDE_SYMBOLS'] == True:
				pass_word+=str(random.choice(symbols))

	print('\nYour password is:')
	for i in pass_word:
		print(i, end='')
		time.sleep(0.01)
	print()