master_pwd = input('what is the master password? ')

def view():
		with open('passwords.txt', 'r') as f: 
			for line in f.readlines():
				#print(line.rstrip) # rstrip to remove the character '\n from the file
				data = line.rstrip()
				user, passw = data.split('|')
				# 'Money|loves|me --> ['Money', 'loves', 'me']
				print('User: ', user, ', Password', passw)
def add():
	name = input('Account Name: ')
	pwd = input('Password: ')

	with open('passwords.txt', 'a') as f: 
		# (name of the file, mode of the file)
		# a --> add , r --> read ,w--> write after erasing 
		f.write(name + '|' + pwd + '\n')


while True:
	mode = input('would you like to add new password \
	or view an existing one (view, add), press q to quit: ').lower()
	if mode == 'q':
		break
		 
	if mode == 'view':
		view()
		
	elif mode == 'add':
		add()

	else:
		print ('Invalid mode.')
		continue

	













