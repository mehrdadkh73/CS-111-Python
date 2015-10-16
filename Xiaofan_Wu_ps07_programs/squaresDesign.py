#Xiaofan Wu
#CS 111 Problem set 7
#squaresDesign


from cs1graphics import*


def squares(levels,size,clr1,clr2,clr3):
    #create a new layer
    allsquare=Layer()
    # if the level is 0, return the empty layer
    
    if levels==0:
        return allsquare
    else:
       #draw the first big square
        firstsquare=Rectangle(size,size, Point(size/2,size/2))
        #set its fillcolor 
        firstsquare.setFillColor(clr1)
        #add the first square
        allsquare.add(firstsquare)
        #draw the second square with a different color by recursively calling
        #the function 
        secondsquare=squares(levels-1,size/2,clr2,clr1,clr3)
        #add the second square to the layer
        allsquare.add(secondsquare)
        #move the second square according to the reference point of the first
        #square. This one is at the bottom of the first square
        secondsquare.moveTo(0,size)
        #draw the third square with a different color by recursively calling
        #the function 
        thirdsquare=squares(levels-1,size/2,clr3,clr2,clr1)
        #add the third square to the layer
        allsquare.add(thirdsquare)
        #move the third layer, this one is the one on the right 
        thirdsquare.moveTo(size,0)

        
        return allsquare

        

        
       
def testSquares(levels, size, clr1, clr2, clr3):
    title = ('testSquares(' + str(levels) + ', ' + str(size) + ', '
              + str(clr1) + ', ' + str(clr2) + ', ' + str(clr3) + ')')
    paper = Canvas(size*2, size*2, 'white', title)
    paper.add(squares(levels, size, clr1, clr2, clr3))
    
testSquares(5, 256, 'darkgreen', 'gold', 'magenta') 