'''Implementation of the Sorto letter game created by Lyn that is a simplified 
   version of Rack-o. Gives lots of practice with while loops and mutable lists.'''
#Xiaofan Wu and Yuanzhen Pan
#CS 111 Problem Set 5
#sorto
import random

allLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # A string of all capital letters
handSize = 8 # Global variable for size of hand used by various functions. 
             # Default is 8. 

# **********************************************************************
# isWinningHand
# **********************************************************************
# Returns True if the letters in hand are in increasing dictionary order. 
# and false otherwise.       
def isWinningHand(hand):
    #find out if the next element is smaller than the previous one, return 
    #false if it is the case. Else return true.
    for i in range(0,len(hand)-1):
        if hand[i]>hand[i+1]:
            return False
    return True


# **********************************************************************
# drawRandomLetter
# **********************************************************************
# Assume letters is a nonempty list of letters. 
# Remove and return a randomly chosen letter from the list.     
def drawRandomLetter(letters):
    #use the index to choose the letters and delete the letter chosen from
    #the letter list. Finally then,return individual letter chosen.
    n=letters.pop(random.randint(0,len(letters)-1))
    return n


# **********************************************************************
# dealHand
# **********************************************************************
# Assume letters is a nonempty list containing at least handSize letters. 
# Return a list of handSize letters randomly chosen and removed from 
# the list of letters. After dealHand returns, letters has handSize
# fewer elements than it did when dealHand was called.   
def dealHand(letters):
    
    newlist=[]
    i=handSize
    #create a while loop to append the individual letters until the number of
    #letters in the newlist equals to handSize.
    while i>0:
        new=drawRandomLetter(letters)
        #append the individual chosen letters to a new list.
        newlist.append(new)
        i=i-1
    return newlist

# **********************************************************************
# queryPlayerForLetterToReplace
# **********************************************************************
# Assume that playerIndex is either 0 or 1; dealtLetter is a single letter string;
# and hand is the hand associated with the player whose index is playerIndex.
#
# Query the specified player for a letter in hand that should be replaced
# by dealt letter. The player can specify an uppercase or lowercase version
# of the letter to be replaced. If the player specifies a nonletter or a 
# letter not in hand, repeatedly query the player for another replacement 
# letter until a valid one is chosen.
# 
# Modify hand to replace the letter chosen for replacement by the dealt letter,
# and return the letter chosen for replacement. 
#       
def queryPlayerForLetterToReplace(playerIndex, drawnLetter, hand):
    #prompt the user for the letter that he/she wants to replace
    newletter = str.upper(raw_input('Player'+str(playerIndex) + " draws " +
    drawnLetter + "."+ " Which letter should " + drawnLetter+ " replace? "))
    #If the letter chosen is not in hand, invoke the function again.
    if newletter not in hand:
        print (newletter + " is not a valid letter in hand " + str(hand) + 
        "\nPlease try again.")
        queryPlayerForLetterToReplace(playerIndex, drawnLetter, hand)
    else: 
        #if the letter chosen is in the list, replace the letter with the
        #new letter drawn.
        hand[hand.index(newletter)]=drawnLetter
        return newletter
    
  
        
    
# **********************************************************************
# displayGameState
# **********************************************************************.
# Display the state of of the game between two lines of dashes.
# This state includes:
# 1. the letters in the drawPile
# 2. the letters in the discardPile
# 3. the letters in Player0's hand (hands[0])
# 4. the letters in Player1's hand (hands[1])
# Each sequence is letters is displayed as a list of one-character strings
# (Simply use str(letters) to display letters in this format.)      
def displayGameState(drawPile, discardPile, hands):
    print('------------------------------------------' +
    '--------------\nCurrent State of the game:')
    print ('Draw Pile: '+str(drawPile))
    print ('Discard Pile: '+ str(discardPile))
    print ('Player0\'s hand: ' + str(hands[0])) 
    print ('Player1\'s hand: ' + str(hands[1])) 
    print('--------------------------------------------------------')

# **********************************************************************
# playGame
# **********************************************************************
# Plays the letter game once. 
# * The game begins by 
#   + Printing a welcome message with the current global handSize
#   + Creating a deck (a list initially containing all upper case alphabetic letters). 
#   + Creating a two-element hands array in which
#     - hands[0] is Player0's hand
#     - hands[1] is Player1's hand
#     - each hand is a list of handSize elements randomly dealt from the deck
#   + Creating an empty discard pile (a list).
#   + Setting the initial draw pile to be the remainder of the deck.
#   + Specifying that Player0 has the first turn
# * At each step of the game: 
#   + The state of the game is displayed.
#   + A random letter is drawn from the draw pile 
#   + The current player chooses which letter from that player's
#     hand will be replaced by the drawn letter. 
#   + The replaced letter is added to the end of the discard pile. 

#   + If the draw pile is empty, the discard pile becomes the new draw pile,
#     and a new empty discard pile is created. 
#   + The other player is specfied to have the next turn
# * The game continues until at least one player has a hand in sorted order. 
#   At that point:
#   + The final state of the game is displayed
#   + If both players have sorted hands, the game is declared a tie.
#     (This can only happen in the rare circumstance in which both
#      players are dealt sorted hands at the very beginning of the game.)
#   + If one player has a sorted hand, that player is declared the winner.
def playGame():
    print('Beginning a new game with handSize '+ str(handSize))
    #  create a deck that includes all the letters in the letter list.
    deck = list(allLetters)
    #  create each player's hand by invoking dealHand function.
    hand0=dealHand(deck)
    hand1=dealHand(deck)
    
    newhand=[]
    newhand.append(hand0)
    newhand.append(hand1)
    
    # create a discard pile
    discardPile=[]
    drawPile=deck
    currentplayer=0
    while not isWinningHand(newhand[0]) and not isWinningHand(newhand[1]):
        displayGameState(drawPile, discardPile, newhand)
        drawnLetter=drawRandomLetter(drawPile)
        letterthatdonotwant=queryPlayerForLetterToReplace(currentplayer,
        drawnLetter, newhand[currentplayer])
        discardPile.append(letterthatdonotwant)
        
        # If the draw pile is empty, the discard pile becomes the new draw pile,
        # and a new empty discard pile is created. 
        if len(drawPile)==0:
            drawPile=discardPile
            discardPile=[]
        
        # alternating players    
        if currentplayer==0:
            currentplayer=1
        else:
            currentplayer=0
            
     # determine who wins and print the appropriate message.       
    displayGameState(drawPile, discardPile, newhand)
    if isWinningHand(newhand[0]):
        displayGameState(drawPile, discardPile, newhand)
        print ("Player0 wins!")
    elif isWinningHand(newhand[1]):
        displayGameState(drawPile, discardPile, newhand)
        print ("Player1 wins!")
    else:
        displayGameState(drawPile, discardPile, newhand)
        print ("The game is a tie!")
        
    # prompt the user to play again after the game ends
    final=raw_input("Do you wish to play again? " + 
    "(Y or y for Yes, anything else for No) ")
    if str.upper(final)=="Y":
        print handSize
        start(handSize)
    else:
        print ("Thank you for playing Sorto!")
            

        
    
    
  
     
# **********************************************************************
# start
# **********************************************************************
# Plays a series of letter games that use size as the handSize.
#
# At the end of each game, prompts the players if they want to play 
# another game. If 'Y' or 'y' is entered, a new game is played;
# Otherwise the start function ends after printing a thank you message. 
#
# size should be an integer between 2 and 12 (inclusive);
#   if these requirements aren't satisfied, the start function
#   displays an appropriate error message and stops. 
#
def start(size):
    # define handsize as global
    global handSize
    #check if the size is an integer and is between 2 and 12 inclusive.
    if isinstance(size,int) and (size<=12 and size>=2):
        handSize=size
        playGame()
    else:
        print ("Error! Hand size " +str(size)+ 
        " is invalid; it must be an integer between 2 and 12, inclusive.")
    
    
    
      
# Sample calls to start. 
# It is recommend that you do initial testing with very small hand sizes. 
#
# start(2) 
#start(3.9) 
#start(3) # 8 is the default hand size, but can play any hand size 2 through 12
# start(12) 
#start('eight')
#start(3.141)
# start(1)
# start(13)

