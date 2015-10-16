#Xiaofan Wu
#CS 111 PS 10
# Bee animation

import Tkinter as tk
import animation
import random
import fruit

class Bee(animation.AnimatedObject):

    def __init__(self, canvas, x, y, size, color1, color2, isFacingRight):


        # Variables needed to draw the bee
        self.size = size
        self.canvas = canvas       
        self.deltax = min(max(10-size/10, 1), 10)  # Speed is a function of size        self.canvas = canvas
        self.color1 = color1
        self.color2 = color2
        
        # Variables needed to update state in *move* method
        self.x = x
        self.y = y        # Not needed right now, but may be useful in child classes
        self.isFacingRight = isFacingRight
        
        # Let's draw the bee
        body = self.canvas.create_oval(x-size, y-size, x+size, y+size, fill = color1)
        stripe1 = self.canvas.create_rectangle(x-0.5*size, y-0.85*size, x-0.4*size, y+0.85*size, fill = color2)
        stripe2 = self.canvas.create_rectangle(x-0.15*size, y-(size-1), x+0.15*size, y+size-1, fill = color2)
        stripe3 = self.canvas.create_rectangle(x+0.5*size, y-0.85*size, x+.6*size, y+0.85*size, fill = color2) 

        # Add wings
        wing1 = self.canvas.create_oval(x-.8*size, y-1.6*size, x+.4*size, y-.4*size, outline = 'black', width = 2.0)
        wing2 = self.canvas.create_oval(x-.93*size, y-1.35*size, x+.27*size, y-.15*size, outline = 'black', width = 2.0)
        
        leftwing1 = self.canvas.create_oval(x-.4*size, y-1.6*size, x+.8*size, y-.4*size, outline = '', width = 2.0)
        leftwing2 = self.canvas.create_oval(x-.27*size, y-1.35*size, x+.93*size, y-.15*size, outline = '', width = 2.0)
        # Add stinger
        stinger = self.canvas.create_polygon(x-size, y-2, x-size, y+2, x-1.5*size,y, fill = 'black')
        leftstinger = self.canvas.create_polygon(x+size, y-2, x+size, y+2, x+1.5*size,y, fill = '')
        
        # Add head
        head = self.canvas.create_oval(x+0.4*size, y-.9*size, x+1.4*size, y+.1*size, fill = color1, outline = 'black')
        lefthead = self.canvas.create_oval(x-1.4*size, y-.9*size, x-.4*size, y+.1*size, fill = '', outline = '')
        
        self.parts = [body, stripe1, stripe2, stripe3, wing1, wing2, head, stinger, leftwing1, leftwing2, lefthead, leftstinger]

        # Set direction
        if not self.isFacingRight:  # Need to change direction bee is facing
            self.flip()
            



    def flip(self):
        # Flip.  Kate O'Hanlon inspired this sneaky trick for flipping:
        if self.isFacingRight:
            self.canvas.itemconfig(self.parts[4], outline='') # make wing1 transparent
            self.canvas.itemconfig(self.parts[5], outline='') # make wing2 transparent
            self.canvas.itemconfig(self.parts[6], fill='', outline='') # make head transparent
            self.canvas.itemconfig(self.parts[7], fill='') # make stinger transparent
            self.canvas.itemconfig(self.parts[8], outline='black') # make leftwing1 show
            self.canvas.itemconfig(self.parts[9], outline='black') # make leftwing2 show
            self.canvas.itemconfig(self.parts[10], fill=self.color1, outline='black') # make lefthead show
            self.canvas.itemconfig(self.parts[11], fill='black') # make leftstinger show
        else:
            self.canvas.itemconfig(self.parts[4], outline='black') # make wing1 show
            self.canvas.itemconfig(self.parts[5], outline='black') # make wing2 show
            self.canvas.itemconfig(self.parts[6], fill=self.color1, outline='black') # make head show
            self.canvas.itemconfig(self.parts[7], fill='black') # make stinger show
            self.canvas.itemconfig(self.parts[8], outline='') # make leftwing1 transparent
            self.canvas.itemconfig(self.parts[9], outline='') # make leftwing2 transparent
            self.canvas.itemconfig(self.parts[10], fill='', outline='') # make lefthead transparent
            self.canvas.itemconfig(self.parts[11], fill='') # make leftstinger show 
        self.isFacingRight = not self.isFacingRight
                   
    def move(self):
        #for part in self.parts:
        #    self.canvas.move(part, self.deltax, 0)
        if self.isFacingRight:
            if self.x+1.45*self.size > self.canvas.winfo_width():
                self.flip()
            else:
                for part in self.parts:
                    self.canvas.move(part, self.deltax, 0)
                self.x += self.deltax
        else:
            if self.x-1.45*self.size < 0:
                self.flip() 
            else:
                for part in self.parts:
                    self.canvas.move(part, -self.deltax, 0)
                self.x -= self.deltax
           

class BusyBee(Bee):
    #call the move method, so that the bee keep moving.
    def move(self):
        Bee.move(self)
        #get a random integer, so that chance is 10%. 10% of the time,
        #The bee will flip its direction and then keep moving. 
        chance=random.randint(1,10)
        if chance==2:
            Bee.flip(self)
       

class FruitBee(Bee):
    #call the move method and keep the bee moving. 
    def move(self):
        Bee.move(self)
        #geta random integer, so that 2% of the time the bee drops fruit.
        chance=random.randint(1,50)
        if chance==2:
            #get four numbers and make it, so that the chance of drop each 
            #fruit is random.
            fruitchance=random.randint(0,3)
            #25% of the time, different fruit that will be droped. I set 
            #the fruit to be dropped from the x and y position of the bee
            #and make the fruit have different weight, so they drop at 
            #different speed
            if fruitchance==0:
                self.canvas.addItem(fruit.Apple(self.canvas,self.x,self.y,5))
            elif fruitchance==1:
                self.canvas.addItem(fruit.Orange(self.canvas,self.x,self.y,10))
            elif fruitchance==2:
                self.canvas.addItem(fruit.Grapes(self.canvas,self.x,self.y,2))
            elif fruitchance==3:
                    self.canvas.addItem(fruit.Banana(self.canvas,self.x,self.y,2))

                
             
                

                
                
                
            
    
