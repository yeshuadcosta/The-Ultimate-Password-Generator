import sys

import pass_word
import pass_phrase

print('***********************************')
print('* THE ULTIMATE PASSWORD GENERATOR *')
print('***********************************')
print()

# Continue this program until the user wants to exit
while True:
	# User Validation for choice
	while True:
		choice = input('Would you like to generate a password or a passphrase?: ').lower()
		if choice == 'password' or choice == 'passphrase':
			break
		else:
			print('Please enter either "password" or "passphrase"!\n')
	if choice == 'password':
		pass_word.uInput()
	elif choice == 'passphrase':
		pass_phrase.uInput()
		
	# Generating a new password
	while True:
		task = input('Would you like to generate a new password? (y/n): ').lower()
		if task == 'y' or task =='n':
			break
		else:
			print('Please enter either "y" or "n"!\n')
	if task == 'y':
		continue
	elif task == 'n':
		print('Termiantion Initiated!')
		sys.exit()