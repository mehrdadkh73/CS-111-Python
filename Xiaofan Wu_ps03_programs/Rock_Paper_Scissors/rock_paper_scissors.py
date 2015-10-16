# Xiaofan Wu
# CS111 Problem Set 3
# Rock/Paper/Scissors Game

import random


#Returns True if gesture is one of the 
# strings 'rock', 'paper', or 'scissors',
# and False otherwise. 
 
def isValidGesture(gesture):
    if (gesture =='rock' or gesture =='paper' or gesture =='scissors'):
        return True
    else:
        return False
        
        

# Randomly returns one of 'rock', 'paper', or 'scissors', with 
# equal probability by using random interger functyion

def randomGesture():
    
    string=['rock', 'paper','scissors']
    string2=string[random.randint(0,2)]
    return string2
    
    
# Returns True if the first gesture beats the second gesture,
# i.e., if the first and second gesture are rock/scissors or
# scissors/paper or paper/rock, respectively. Returns False otherwise.

def beats(gesture1, gesture2):
   
         
    if (gesture1=='rock' and gesture2=='scissors'):
        return True
    elif (gesture1=='scissors' and gesture2=='paper'):
        return True
    elif (gesture1=='paper' and gesture2=='rock'):
        return True
    else:
        return False
    
    

# Plays rock/paper/scissors game with your gesture vs. opponent's gesture.
# If both gestures are valid, displays one of 'Tie game!', 'You win!',
# or 'Opponent wins!'. Otherwise, indicates which gesture is invalid.

def play(you, opponent):
    
    #First check if the gesture is valid 
    if not isValidGesture(you):
        print('Your gesture(' + you + ') is invalid')
    #Then check if the opponent's gesture is valid
    elif not isValidGesture(opponent):
         print ("opponent's gesture gesture(" + opponent + ") is invalid")
    #After verifying, invoke the beat function to figure out who win.        
    elif beats(you,opponent):
            print ("You win!")
        
    elif you==opponent:
            print("Tie game!")
    else:
            print ("opponent wins")
        


# Plays rock/paper/scissors against a computer opponent that
# randomly chooses a gesture. First displays the choice of the computer,
# and then displays the result of the game.

def playComputer(you):
    #Invoke randomGesture function to produce a random number
    computer=randomGesture()
    print ("Computer chooses " + computer)
    #Invoke the play function to let the you and computer play.
    play(you,computer)
    
