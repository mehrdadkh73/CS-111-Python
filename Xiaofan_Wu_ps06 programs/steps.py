#Xiaofan Wu
#CS 111 Problem set 6
#steps 

from turtle import*
#make the background color black and default pen color white
bgcolor('black')
pencolor('white')
#Speed is set to fastest
speed(0)   
#Bring the canvas to the front
getscreen()._root.attributes('-topmost', True)
getscreen()._root.attributes('-topmost', False)

# Draw the individual square
def square(length):
    """draws a square of size length maintains heading 
       and position invariant"""
    for i in range(1,5): # or for i in range(4)
        fd(length)
        lt(90)
# Create each row      
def row(number,size,clr1,clr2):
    #if number>0 is the baseline
    if number>0: 
        #draw the first square in clr1
        pencolor(clr1)
        square(size)
        pu()
        fd(size+size/4)
        pd()
        #draw the second square in clr2 by switching the order and calling 
        #the row function 
        row(number-1,size,clr2,clr1)
        #make sure that the row is invariant 
        pu()
        bk(size+size/4)
        pd()
# draw the steps 
def steps(number,size,clr1,clr2):
    #if number>0 is the baseline
    if number>0:
        #draw the steps by calling row function 
        row(number,size,clr1,clr2)
        #since the row function is invariant already, the turtle will be 
        #back to its original position. The only thing needed to do it 
        #to move the turtle up to the second row.
        pu()
        lt(90)
        fd(size+size/4)
        rt(90)
        pd()
        #draw the second row with a different color by invoking row function
        #that switched the position of the color called. Also the number of 
        #row is one less
        steps(number-1,size,clr2,clr1)
        pu()
        lt(90)
        bk(size+size/4)
        rt(90)  
        pd()
        
#Testing function        
steps(8,30,'red','blue')

