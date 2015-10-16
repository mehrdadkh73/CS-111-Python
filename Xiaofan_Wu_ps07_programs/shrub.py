#Xiaofan Wu
#CS 111 Problem set 7
#Turtle Shrubs

from turtle import*

def shrub(trunkLength,angle,shrinkFactor,minLength):
    if minLength>trunkLength:
        return (0,0)
    else: 

        fd(trunkLength)
        rt(angle)
        (numBranches1, branchLen1) = shrub(trunkLength*shrinkFactor,angle,shrinkFactor,minLength)
        lt(angle*2)
        (numBranches2, branchLen2) = shrub(trunkLength*shrinkFactor*shrinkFactor,angle,shrinkFactor,minLength)
        rt(angle)
        bk(trunkLength)
        numBranches=numBranches1+numBranches2+1
        branchLen=branchLen1+branchLen2+trunkLength
        return (numBranches,branchLen)
        
# Testing code for shrub function. 
# Need to close the window before result will be printed. 
def testShrub (trunkLength, angle, shrinkFactor, minLength):
    setup(600, 400) # Make the turtle window be 600 x 400
    
    # Magical incantation to bring turtle window to top of screen.
    getscreen()._root.attributes('-topmost', True)
    getscreen()._root.attributes('-topmost', False)

    #bgcolor('yellow')  # Set the background color

    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal  

    pensize(1) # Choose a size you like      

    # Move turtle to lower middle pointing up 
    setpos(0, -(window_height()/2.0 - 20))
    setheading(90)

    clear() # Clear any existing turtle drawings
    
    testInputString = ('shrub(' + str(trunkLength) + ', ' 
                       + str(angle) + ', ' + str(shrinkFactor) 
                       + ', ' + str(minLength) + ')')

    # Put testInputString in title at top of window
    title(testInputString)
      
    # Draw shrub and put result in answerTuple 
    answerTuple = shrub(trunkLength, angle, shrinkFactor, minLength)
    
    
    testOutputString = testInputString + ' -> ' + str(answerTuple)
            
    # Put testOutputString in title at top of window
    title(testOutputString)

    # Print testOutputString in console
    print(testOutputString)
     
    # Declare that drawing is done 
    # (allows closing window and printing results)  
    done() 
testShrub(100, 15, 0.8, 10)