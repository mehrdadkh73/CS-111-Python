#Xiaofan Wu and Amy Yuan
#CS 111 problem set 3
#tangentCircles
from cs1graphics import*


def tangentCircles(size, numCircles, colorList):
    #create a canvas that is size x size and name it accordingly
    paper=Canvas(size,size,"white", "tangentCircles("+str(size)+"," + 
    str(numCircles)+"," + str(colorList) + ")" )
    
    for i in range (1,numCircles+1):
        #Figure the radium of the smallest cirlce
        r=(size/2.0)/numCircles
        # i ranges from 1 to how many circles there are plus 1. Using this 
        #equation, find out the radium of each circle
        r2=i*r
        #Draw the circles 
        circle=Circle(r2)
        #adjust reference point to the top of the circle
        circle.adjustReference(0,-r2)
        #move the circle to the top of the canvas
        circle.moveTo(size/2,0)
        #set depth of the circle, so the bigger circle does not cover the 
        #small ones
        circle.setDepth(i)
        #Fill the color of the circle using index of colorList
        circle.setFillColor(colorList[((i) % len(colorList)-1)])
        paper.add(circle)


#Test cases
tangentCircles(500, 6, ['cyan'])

tangentCircles(500, 10, ['green', 'yellow']) 

tangentCircles(500, 20,['red', 'magenta', 'blue'])    
        
     