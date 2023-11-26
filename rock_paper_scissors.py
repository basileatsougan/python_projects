
import random

def play():
	user = input("What's your choice ? \n'r' for Rock, 'p' for Paper and 's' for scissors : ")
	computer = random.choice(['r', 'p', 's'])

	if user == computer:
		return 'It\'s a tie'

	if is_win(user, computer):
		return f'The computer choosed {computer}. \nWonderful! You beat the computer'

	return 'You lost unfornately against the computer'


def is_win(user, computer):
	# r>s, s>p, p>r
	if ((user == 'r' and computer == 's') or (user == 's' and computer == 'p' ) or (user == 'p' and computer == 'r')):
		print(f'You have choosen {user} and the computer has choosen {computer}')
		return True


print(play())