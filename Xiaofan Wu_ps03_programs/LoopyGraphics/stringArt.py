#Xiaofan Wu and Amy Yuan
#CS 111 problem set 3
#StringArt


from cs1graphics import *
import random
import math

def stringArt(size, pointList, colorList):
    
    # Creates a size x size white canvas 

    paper=Canvas(size,size,"white","StringArts")
    
    # create radius-5 circles centered at each point in pointList.
    
    for i in pointList:
        circle=Circle(5,i)
        paper.add(circle)
        
    #Loop the color of the lines. The first color is associated with a polygon
    #with increment 1, the second color is the color of the polygon with 
    #increment 2. 
    
    for i in range(len(colorList)):
        polygon=stringPolygon(i+1,pointList,colorList[i])
  
        paper.add(polygon)
    

def stringPolygon(increment, pointList, color):
    #create a polygon
    p=Polygon() 
    #Using the length of the pointlist, visit the each point first with 
    #increment 1, then the increment is multiple of an interger from 1 to 
    #how many points there are. 
    # When n is 8 and increment is 2, the Polygon will appear to have 4 lines,
    # and when n is 8 and increment is 4, the Polygon will appear to have a 
    # single line. 
    
    for i in range(len(pointList)):
        # "%" wraps the index back to the beginning of the index list
        p.addPoint(pointList[i*increment%len(pointList)]) 
    p.setBorderColor(color)

    return p
        
        
# Returns a list with numPoints points arranged equidistantly 
# around a circle with the given radius centered at (x,y)    
#code was given
def makeCircularPoints(numPoints, x, y, radius):
    pointList = []
    angle = 2*math.pi/numPoints # in radians
    for i in range(0, numPoints):
        pointList.append(Point(x + radius*math.cos(i*angle),
                               y + radius*math.sin(i*angle)))
        
    return pointList



# Test cases:

stringArt(500, 
          [Point(100,100), Point(100,300), Point(250,400),
           Point(400,300), Point(400,100)],
          ['red','blue'])    
stringArt(500, makeCircularPoints(7, 250, 250, 225), 
          ['red', 'green', 'blue'])
stringArt(500, makeCircularPoints(8, 250, 250, 225), 
          ['red', 'green', 'blue', 'magenta'])
stringArt(500, makeCircularPoints(13, 250, 250, 225), 
          ['red','blue','green','magenta','cyan'])

