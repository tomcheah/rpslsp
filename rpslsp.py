from random import *

list_of_choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
player_score = 0 
computer_score = 0

def pick_choice():
	number = randint(0, 4)
	return list_of_choices[number]

def start_game():
	print('Welcome to Rock-Paper-Scissors-Lizard-Spock!')
	play()

def play():
	print('Type in a choice from ' + str(list_of_choices) + '.')
	user_choice = input()
	computer_choice = pick_choice()
	print('The computer chooses ' + str(computer_choice
		) + '.')
	rules(user_choice, computer_choice)
	print('Player score: ' + str(player_score) + ', Computer score: ' + str(computer_score))
	replay()

def rules(user_choice, computer_choice):
	global player_score, computer_score
	if user_choice == 'rock':
		if computer_choice == 'scissors' or computer_choice == 'lizard':
			print('Rock beats ' + str(computer_choice
				) + '.')
			player_score += 1
		elif computer_choice == 'rock':
			print("It's a tie! Rocks don't beat rocks.")
		else:
			print(str(computer_choice) + ' beats rock.')
			computer_score += 1
	elif user_choice == 'paper':
		if computer_choice == 'spock' or computer_choice == 'rock':
			print('Paper beats ' + str(computer_choice
				) + '.')
			player_score += 1
		elif computer_choice == 'paper':
			print("It's a tie! Papers don't beat papers.")
		else:
			print(str(computer_choice) + ' beats paper.')
			computer_score += 1
	elif user_choice == 'scissors':
		if computer_choice == 'paper' or computer_choice == 'lizard':
			print('Scissors beats ' + str(computer_choice
				) + '.')
			player_score += 1
		elif computer_choice == 'scissors':
			print("It's a tie! Scissors don't beat scissors.")
		else:
			print(str(computer_choice) + ' beats scissors.')
			computer_score += 1
	elif user_choice == 'lizard':
		if computer_choice == 'paper' or computer_choice == 'spock':
			print('Lizard beats ' + str(computer_choice
				) + '.')
			player_score += 1
		elif computer_choice == 'lizard':
			print("It's a tie! Lizards don't beat lizards.")
		else:
			print(str(computer_choice) + ' beats lizard.')
			computer_score += 1
	elif user_choice == 'spock':
		if computer_choice == 'scissors' or computer_choice == 'rock':
			print('Spock beats ' + str(computer_choice
				) + '.')
			player_score += 1
		elif computer_choice == 'spock':
			print("It's a tie! Spocks don't beat spocks.")
		else:
			print(str(computer_choice) + ' beats spock.')
			computer_score += 1

def replay():
	play()