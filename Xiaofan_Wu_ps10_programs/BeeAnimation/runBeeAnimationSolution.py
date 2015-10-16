# Runs a sample solution of the Bee animation
import Tkinter as tk
#changed all the place that had Bee.Sol to only bee, because we only want to 
#use our own solution for bee.
import bee
import animation
import os
 
# TESTING
WIDTH = 500
HEIGHT = 300
BACKGROUNDCOLOR = 'deepskyblue'
    



class App(object):
    def __init__(self, master, **kwargs):
        self.master = master        
        self.frame = tk.Frame(root) 
        self.frame.pack()             
        self.canvas = animation.AnimationCanvas(self.frame, width=WIDTH, height=HEIGHT, bg=BACKGROUNDCOLOR) 
        self.canvas.pack()
        # Here we build an animation by adding several AnimatedObjects to the AnimationCanvas
        self.canvas.addItem(bee.FruitBee(self.canvas, 200, 40, 10, 'yellow', 'black', True))
        self.canvas.addItem(bee.fruit.Apple(self.canvas, 120, 120, 1))
        self.canvas.addItem(bee.FruitBee(self.canvas, 180, 180, 40, 'darkgray', 'pink', False))
        self.canvas.addItem(bee.Bee(self.canvas, 250, 250, 10, 'yellow', 'black', True))
        self.canvas.addItem(bee.BusyBee(self.canvas, 100, 100, 50, 'blue', 'red', False))
        self.canvas.addItem(bee.BusyBee(self.canvas, 200, 200, 20, 'darkgreen', 'magenta', True))
        tk.Button(root, text="Stop", command=self.canvas.stop).pack()
        tk.Button(root, text="Go", command=self.canvas.start).pack()     


root = tk.Tk()
root.title("BeeCanvas")
app = App(root)
# For Macs only: Bring root window to the front
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


root.mainloop()    



