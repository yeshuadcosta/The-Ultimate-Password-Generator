import random
import time

options = {
	'WORD_COUNT': 0,
	'INCLUDE_NUM': False,
	'INCLUDE_SYMBOLS': False
}

def uInput():
	global options

	# Accept the word count as user input
	while True:
		options['WORD_COUNT'] = int(input('Enter the number of words: '))
		if options['WORD_COUNT'] >= 1:
			break
		else:
			print('The number of words should be greater than "0"!\n')

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

	# Asking the user to choose a one character deliminator
	delim = ''
	while True:
		delim = input('Enter a one character deliminator: ')
		if len(delim) == 1 or len(delim) == 0:
			break
		else:
			print('The deliminator chosen should be a single charcacter!\n')

	# Extract the words from words.txt #
	words_file = open('words.txt', 'r')
	words = []
	while True:
		line = words_file.readline().strip()
		if len(line) == 0:
			break
		else:
			words.append(line)
	#----------------------------------#

	symbols = ('!','@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']','.','<', '>', '?', '/', '|', '\\', ';', ':', ',', '~', '`', "'", '"')
	create(words, symbols, delim)

def create(words, symbols, delim):
	global options
	
	pass_words = []
	for i in range(options['WORD_COUNT']):
		pass_words.append(random.choice(words))

	# Include numbers if opted for
	num_words = []
	if options['INCLUDE_NUM'] == True:
		for i in range(options['WORD_COUNT']):
			num_words.append(random.randint(1, 100))

	# Include symbols if opted for
	sym_words= []
	if options['INCLUDE_SYMBOLS'] == True:
		for i in range(options['WORD_COUNT']):
			sym_words.append(random.choice(symbols))

	passphrase = ''
	order = []
	for x in range(options['WORD_COUNT']):
		# Generating the order
		while True:
			num = random.randint(1,3)
			if num not in order:
				order.append(num)
			if len(order) == 3:
				break

		for i in order:
			if i == 1:
				passphrase+=pass_words[x]
			elif i == 2:
				if options['INCLUDE_NUM'] == True:
					passphrase+=str(num_words[x])
			elif i == 3:
				if options['INCLUDE_SYMBOLS'] == True:
					passphrase+=sym_words[x]
		if x != options['WORD_COUNT'] - 1:
			passphrase+=delim
		order = []

	print('\nYour password is:')
	for i in passphrase:
		print(i, end='')
		time.sleep(0.01)
	print()