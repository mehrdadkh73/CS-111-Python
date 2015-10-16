#Xiaofan Wu
#CS111 Problem set 6
#Rectangle
# Create a function that takes four parameters

def rectangle(width,height,char1,char2):
     #Create a baseline for the function and the baseline is if height>0
     
     if height>0:
        #Print out one line of char1 multiplied by the width
        print char1*width
        #reduce height by one, so each time the function is invoked, it is 
        #invoking one less. 
        height=height-1
        #invoke the function, but switch the position of char 2 and char1
        #so the invocation calls different character each time 
        rectangle(width,height,char2,char1)
#testing functions
rectangle(5, 8, 'X', 'O')
rectangle(7, 5, '~', '+')