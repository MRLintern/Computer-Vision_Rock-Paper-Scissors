#base code for R-P-S game
#this will be developed further
#for ML cases

import random 
#make use of enum class. 
#working with strings can cause problems.
#working with numbers is more efficient.
from enum import IntEnum 

#the program allows for multiple games of R P S


class Action(IntEnum):

	Rock = 0
	Paper = 1
	Scissors = 2
	
#function to get human player's choice
def human_choice():
	"""
	
	function to gather humans choice in action: rock, paper or scissors
	a list will be generated giving the users choice in action and the 
	value associated with the chosen action.
	e.g. action.name = Rock and Rock has a value of 0
	
	"""
	
	available_choices = [f"{action.name}[{action.value}]" for action in Action]
	choices_str = ", ".join(available_choices)
	selection = int(input(f"Enter a choice ({choices_str}): "))
	action = Action(selection)
	return action
	
#function to get computer's choice
def computer_choice():

	"""
	this performs in a similar way to user_choice() 
	the computer will generate a choice at random
	
	"""
	
	selection = random.randint(0, len(Action) - 1)
	action = Action(selection)
	
#function to determine whether the human or computer wins
def who_wins(human_action, computer_action):

	if human_action == computer_action:
		print(f"The human and the computer selected {human.action.name}. The game is a draw.")
	elif human_action == Action.Rock:
		if computer_action == Action.Scissors:
			print("Rock smashes scissors. The human wins.")
		else:
			print("Paper covers rock. The computer wins.")
	elif human_action == Action.Paper:
		if computer_action == Action.Rock:
			print("Paper covers rock. The human wins.")
		else:
			print("Scissors cuts paper. The computer wins.")
	elif human_action == Action.Scissors:
		if computer_action == Action.Paper:
			print("Scissors cuts paper. The human wins.")
		else:
			print("Rock smashes scissors. The computer wins.")
				
while True:

	#pick up errors/problems	
	try:
	
		human_action = human_choice()
	
	except ValueError as e:
	
		range_str = f"[0, {len(Action) - 1}]"
		print(f"Invalid selection. Enter a value in range {range_str}")
		
		continue
		
	computer_action = computer_choice()
	
	#see who wins the game
	who_wins(human_action, computer_action)
	
	play_again = input("Play another game? (y/n): ")
	
	if play_again.lower() != "y":
		break
		
		
		
		
		
		
		
		
		
		
