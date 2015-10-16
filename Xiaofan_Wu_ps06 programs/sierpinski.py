#Xiaofan Wu and Catrina Sun-Tan
#CS 111 Problem set 6
#sierpinski

from turtle import*

#code given

setpos(-(window_width()/2.0 - 20), -(window_height()/2.0 - 20))

# Set the background color and pencolor.
bgcolor('black')
pencolor('white')# Set the background color
speed(0)   
#make sure the canvas appear in the front 
getscreen()._root.attributes('-topmost', True)
getscreen()._root.attributes('-topmost', False)

def sierpinski(level,size):
    #set the base case as level>0
    if level>0:
        #draw one size of the triangle
        sierpinski(level-1,size/2)
        fd(size)
        lt(120)
        #draw another side of the triangle
        sierpinski(level-1,size/2)
        fd(size)
        lt(120)
        #draw the third size of the triangle
        sierpinski(level-1,size/2)
        fd(size)
        lt(120)
# move the starting point        
#pu()
#back(200)
#lt(90)
#back(200)
#rt(90)
#pd()
##testing functions   
sierpinski(5, 400)  

