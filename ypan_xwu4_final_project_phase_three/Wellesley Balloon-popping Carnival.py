# -*- coding: utf-8 -*-

#Xiaofan Wu Yuanzhen Pan 
#CS-111
#Final Project: Balloon Popping Carnival


import Tkinter as tk
import random
import animation


#setm minimal and maximal ball size
MINBALLSIZE, MAXBALLSIZE = 10, 50
#create a dictionary to relate color of the balloon to their speed and points
rainbow = {"red":10, "orange":20, "yellow":30, "green":40, "blue":50, "violet":random.randint(-50, 100) } # make it a dictionary


# create an App class        
class App(tk.Frame):       
    
    #Using the init method and create instance variables that will be useful later on
    def __init__(self, root):
        tk.Frame.__init__(self)
        root.title('Wellesley Balloon Popping Carnival')# set the frame title
        self.grid() 
        self.time=60 #set the time to play this game as 60 (seconds)
        self.createWidgets() 
        self.BalloonsInSky=[] #create an empty list to store information of the balloons
        self.canvas.bind('<Button-1>', self.onClick) 
        #when the user does left click, it invokes onClick funtion
        self.score=0 # set the initial score to be 0
        

    def createWidgets(self):
        #Create the welcome text and out it at the right place on the frame using grid
        self.textLabel=tk.Label(self, text='Welcome to Wellesley Balloon-Popping Carnival', bg='white', font='Verdana 24 bold')
        self.textLabel.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S)
        
        #create a canvas for animation and put it under welcome text using grid
        self.canvas=animation.AnimationCanvas(self,width=400,height=400,bg= 'lightblue')
        self.canvas.grid(row=1,column=0,sticky=tk.N+tk.E+tk.W+tk.S)
        
        #create a button panel 
        buttonPanel = tk.Frame()
        buttonPanel.pack() 
        buttonPanel.grid(row=1,column=0)
        
        #On the button panel
        #create a start button that invokes onStartButtonClick when the user clicks 
        #create a quit button that inokes onQuitButtonClick when the user clicks 
        self.startButton = tk.Button(buttonPanel, text='Start', command=self.onStartButtonClick)
        self.quitButton=tk.Button(buttonPanel,text='Quit',command=self.onQuitButtonClick)
        self.startButton.grid(row=0,column=0)
        self.quitButton.grid(row=0,column=1)
        
        #create a text variable called score to display the score
        self.scores=tk.StringVar()
        self.scoresLabel = tk.Label(self,fg='blue', font='Verdana 12 italic',bg='white',textvariable=self.scores)
        self.scoresLabel.grid(row=2,column=2)
        self.scores.set('Your score is 0')
        
        #create a text variable instruction to display instructions for the game
        self.instruction=tk.StringVar()
        self.instructionLabel = tk.Label(self,fg='blue', font='Verdana 12 italic',bg='white',textvariable=self.instruction)
        self.instructionLabel.grid(row=1,column=2)
        self.instruction.set('The aim of this game is to\n score as many points as possible \n in 1 minute by popping balloons.\n Red =10 pts\n Orange=20 pts\n Yellow=30 pts\n Green=40 pts\n Blue=50 pts\n Violet=any number between -50 to 100 points')

        #create a text variable called timer to display the amount of time left for the game
        self.timer= tk.StringVar()
        self.timerLabel=tk.Label(self, fg='red', bg='white', font='Verdana 24 bold',textvariable=self.timer)
        self.timerLabel.grid(row=0,column=2,sticky=tk.N+tk.E+tk.W+tk.S)
        self.timer.set('You have ' + str(self.time)+' s left!')
        
        
    #define a function called launchBalloon
    #when the funtction is invoked, it invokes the balloon class and create a balloon
    #and append the information of the balloon into BalloonsInSky list
    def launchBalloon(self):
        balloon = Balloon(self.canvas,self.BalloonsInSky)
        self.BalloonsInSky.append(balloon)
        self.canvas.addItem(balloon)
        self.after(500,self.launchBalloon) #invoke the launchBalloon function after every 0.5 seconds


    #define a fuction called onStartButtonClick
    #when the funciton is invoked, it set start the canvas
    #invoke launchBalloon function immediately
    #it will also invoke the UpdateTimer function in App class
    #disable the start button and invoke the endGame function after 60 seconds
    def onStartButtonClick(self):
        self.canvas.start()
        self.after(0,self.launchBalloon)
        self.after(1000,self.UpdateTimer)
        self.startButton.config(state='disabled')
        self.after(60000,self.endGame)
    
    
    #define a fuction called onQuitButtonClick 
    #the function is invoked when the user clicks on the quit button
    #it quits the game 
    def onQuitButtonClick(self):
        root.destroy()   
    
    
    #define a fuction called onClick
    #it loops through the information of every balloon in BalloonsInSky list
    #when the user's click coordinate is within the bounding box of the balloon
    #increase the score by the score of the balloon clicked
    #remove('pop') the balloon from the canvas
    #and update the score text
    def onClick(self,event):
        for balloon in self.BalloonsInSky:
            x1, y1, x2, y2 = self.canvas.bbox(balloon.id)
            if event.x>x1 and event.x<x2 and event.y>y1 and event.y<y2:
                self.score+=rainbow[balloon.color] 
                balloon.remove()
                self.scores.set('Your score is ' + str(self.score))
     
     
    #define a fuction called UodateTimer
    #create a conditional that when the time is greater than zero second, 
    #it keeps updating timer text by decreaing time by 1
    #when the time left reaches 0, the timer text will be set to 'Time is up'
    def UpdateTimer(self):
        self.time -=1
        if self.time>0:
            self.timer.set('You have ' + str(self.time)+' s left!')
            self.after(1000,self.UpdateTimer)
        else:
            self.timer.set('Time is up!')
            

    #define a funciton called endGame
    #when the function is invoked,
    #it sets the canvas background color to white
    #stops the canvas
    #disable the left click
    #and display the final score and message to the player
    def endGame(self):
        self.canvas.config(bg='white')
        self.canvas.stop()
        self.scores.set('Your final score is ' + str(self.score))
        self.canvas.bind('<Button-1>', self.Disable)

        if self.score>1000:
            self.canvas.create_text(300,200, fill='black',font="Purisa 24 bold", text="Your final score is "+ str(self.score)+"! \nYou are a balloon-popping guru! :D")
        else:
            self.canvas.create_text(300,200, fill='black',font="Purisa 24 bold", text="Your final score is "+ str(self.score)+ ". Try harder next time!")
        
        
    def Disable(self,event):
        pass


#create a Balloon class
class Balloon(animation.AnimatedObject):

    def __init__ (self, canvas, balloonList,*args, **kwargs):
    #Use init method to assign variables
    
        #create the variale for the x position of the balloon
        self.x = random.randint(0,400)
        
        #create the canvas
        self.canvas = canvas
        
        #make the y position 50 below the canvas, so they show up at the
        #bottom outside of the canvas.
        self.y = self.canvas.winfo_reqheight()+ 50
        
        #randomly choose a color for the balloon
        self.color = random.choice(rainbow.keys())
        
        #Get the speed of the balloon base on the balloon color
        self.speed = abs(rainbow.get(self.color))*0.1
        self.delta = self.speed 
        
        #randomly generate a number to be the balloon's radius.
        self.radius = random.randint(MINBALLSIZE, MAXBALLSIZE)
        self.balloonList= balloonList
        
        #Create the balloon with variables generated randomly previously.
        self.balloon = self.canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius,outline=self.color,fill = self.color)
        #create the string of the balloon 
        self.string=self.canvas.create_line(self.x,self.y+self.radius,self.x,self.y+self.radius*3,fill = 'black')
        #Create the triangle underneath the balloon 
        self.triangle=self.canvas.create_polygon(self.x,self.y+self.radius,self.x-5,self.y+self.radius+5,self.x+5,self.y+self.radius+5,fill = self.color)
        
        #combine all the parts into one list 
        self.parts = [self.balloon,self.string,self.triangle]
        self.id = self.balloon
        
        
    def move(self):
        #move the whole balloon up by looping through each part in parts
        #the balloon moves up based on the speed generated 
        for part in self.parts:
            self.canvas.move(part, 0, -self.delta) # move up toward ceiling and does not stop even if it reaches the top   
        self.y -= self.delta
        
    def remove(self):
        #remove each part of the balloon by looping through each part in parts
        for part in self.parts:
            self.canvas.delete(part)
        #remove the information of the removed balloon from the balloon list
        self.balloonList.remove(self)
                 

root = tk.Tk()
app = App(root)
app.mainloop()
    