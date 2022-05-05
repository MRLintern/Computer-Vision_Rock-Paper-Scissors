"""
For the actual program need to incorporate the following:
=========================================================

import cv2
from keras.models import load_model
import numpy as np
model = load_model("keras_model.h5")
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

"""

from argparse import Action
import random
import time
from enum import IntEnum

from matplotlib.style import available

################# POTENTIAL COUNTDOWN FUNCTION ##########################
#how do i incorporate this???
def countdown(secs):
    while secs:
        print(secs)
        time.sleep(1)
        secs -= 1

##########################################################################


class Action(IntEnum):
    
    Rock = 0
    Paper = 1
    Scissors = 2
    Nothing = 3
    
#human choice
def human_choice():
    
    available_choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ",".join(available_choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

#computer choice
def computer_choice():
    
    selection = random.randint(0, len(Action)-1)
    action = Action(selection)
    return action

#who wins the game
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
            print("Scissors cuts paper. The human wins")
        else:
            print("Rock smashes scissors. The computer wins.")
    elif human_action == Action.Nothing:
        if computer_action == Action.Nothing:
            print("No choice was made.")
        #the Nothing action doesn't work; take this out and the program works
            
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
	
