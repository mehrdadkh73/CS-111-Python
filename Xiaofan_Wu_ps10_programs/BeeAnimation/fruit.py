#Xiaofan Wu
#CS 111 PS10
# Fruit

import animation
import random

class Fruit(animation.AnimatedObject):
    
    def __init__(self, canvas, x, y, weight):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.weight = weight  # Heavier fruit fall faster
        self.fallenToGround = False
        self.fruitLayer = self.getFruitLayer()
        
    def getFruitLayer(self):
        raise NotImplementedError('*getFruitLayer* method needs to be implemented in class inheriting from Fruit.')
        

    def move(self):
        if self.y < self.canvas.winfo_height()+10:
            for item in self.fruitLayer:
                self.canvas.move(item, 0, self.weight)
            self.y = self.y + self.weight  # Increase y coordinate

        else:
            self.fruitLayer = []   # Hara Kiri
            for item in self.fruitLayer:
                self.canvas.remove(item)


class Apple(Fruit):

    def __init__(self, canvas, x, y, weight): 
        Fruit.__init__(self, canvas, x, y, weight)
           
    def getFruitLayer(self):
        size = 10
        x = self.x
        y = self.y
        theLayer = []
        mac = self.canvas.create_oval(x, y, x+size, y+size, fill='red')  
        stem = self.canvas.create_polygon(x+0.4*size, y, x+0.6*size, y, x+0.5*size, y-0.4/size, x+0.7*size, y-0.4*size, fill = 'darkgreen')
        return [mac, stem]

class Banana(Fruit):

    def __init__(self, canvas, x, y, weight): 
        Fruit.__init__(self, canvas, x, y, weight) 
           
    def getFruitLayer(self):
        size = 30
        x = self.x
        y = self.y
        banana = self.canvas.create_polygon(x, y, x-size/8, y-size/2, x+size/4, y, x-size/8, y+size/4, fill = 'yellow')
        return [banana]

class Grapes(Fruit):

    def __init__(self, canvas, x, y, weight): 
        Fruit.__init__(self, canvas, x, y, weight)
            
    def getFruitLayer(self):
        size = 20
        x = self.x
        y = self.y
        numGrapes = 6
        radius = size/4
        grapes = []
        for i in range(0, numGrapes):
            xc = x+random.randint(-radius, radius)
            yc = y+random.randint(-radius, radius)
            grapes.append(self.canvas.create_oval(xc, yc, xc+2*radius, yc+2*radius, fill = 'purple'))
        return grapes

class Orange(Fruit):
    #create the init method 
    def __init__(self, canvas, x, y, weight): 
        Fruit.__init__(self, canvas, x, y, weight) 
    # create the fruit to be dropped from the bee by calling the oval shape     
    def getFruitLayer(self):
        #start at x and y and the it is 20 to to right side and 20 to the bottom.
        size = 20
        x = self.x
        y = self.y
        theOrange = self.canvas.create_oval(x, y, x+size, y+size, fill='orange')  
        #return the orange. 
        return [theOrange]