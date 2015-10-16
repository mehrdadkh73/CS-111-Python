#Xiaofan Wu 
#CS 111 Problem Set 5
#eggCartons
from cs1graphics import*

def eggCarton (size, eggColumns, eggRows, colorList):
    #caculate the width and height of the egg
    w=(float(size)/eggColumns)
    h=(float(size)/eggRows)
    #create a layer 
    grid = Layer()
    #use nested for loop, so that the column is slower than the row. 
    for col in range(eggColumns):
        for row in range(eggRows):
            #create the ellipse
            ellipse=Ellipse(w,h,Point(w*col+w/2,h*row+h/2))
            #set the fill color by finding out which row the egg is, then add
            #the column number to find where the egg is in that row.
            ellipse.setFillColor(colorList[((eggColumns*row+col)
            % len(colorList))])
            #make an rectangle as the border
            rectangle=Rectangle(size,size,Point(size/2,size/2))
            rectangle.setBorderWidth(3)
            grid.add(rectangle)
            grid.add(ellipse)  
    return grid 

def eggCartonTest(size, cols, rows, colors):
    canvas = Canvas(size, size, 'white', 'Egg Carton Test with ' + str(cols) 
                    + ' columns and ' + str(rows) + ' rows.') 
    canvas.add(eggCarton(size, cols, rows, colors))

threeColors = ['yellow', 'pink', 'cyan']
sevenColors = ['yellow', 'pink', 'cyan', 'red', 'blue','magenta','green']

# Sample tests with eggCartonTest
eggCartonTest(400,1,1,threeColors)
eggCartonTest(400,5,1,threeColors)
eggCartonTest(400,1,5,threeColors)
eggCartonTest(400,5,3,sevenColors)
eggCartonTest(400,3,5,sevenColors)


def cartonGrid (cartonSize, gridColumns, gridRows, colorList):
    paper=Canvas(cartonSize*gridColumns,cartonSize*gridRows,"white",
    "Egg Carton Grid with " 
    + str(gridColumns) + " columns and " + str(gridRows) + " rows.")
    #create a nested loop, so that the row runs slower than the column.
    for i1 in range (gridRows+1):
        for i in range (gridColumns+1):
            #create the eggs in each egg carton 
            eggs=eggCarton(cartonSize, i+1,i1+1,colorList)
            #move the eggcarton to apporiate place by  multiplying the size of 
            #the carton to the increase of rows and columns
            eggs.moveTo(cartonSize*i,cartonSize*i1)
            paper.add(eggs)

#or this way will work too. 
#def cartonGrid (cartonSize, gridColumns, gridRows, colorList):
#    paper=Canvas(cartonSize*gridColumns,cartonSize*gridRows,"white", 
#"Egg Carton Grid with " 
#    + str(gridColumns) + " columns and " + str(gridRows) + " rows.")
#    for i1 in range (1,gridRows+1):
#        for i in range (1,gridColumns+1):
#
#            eggs=eggCarton(cartonSize, i,i1,colorList)
#            eggs.moveTo(cartonSize*(i-1),cartonSize*(i1-1))
#            paper.add(eggs)
#    
            
        
            
        

cartonGrid(125, 6, 4, sevenColors)
            
