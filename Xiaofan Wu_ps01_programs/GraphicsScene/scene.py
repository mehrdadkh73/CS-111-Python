#----Xiaofan Wu and Yuanzhen Pan
#----CS111 Pset1 
#----Title: Moonlight Camping Site

from cs1graphics import *

#----Make the background 
paper = Canvas(1000,600,"blue1","night sky with stars at a camping site")

#----Make the mountains 
mountain1 = Ellipse(300,500, Point(200,400))
mountain1.setFillColor("lightsalmon4") 
mountain1.setBorderColor("lightsalmon4") 
paper.add(mountain1) 

mountain2 = mountain1.clone() 
mountain2.moveTo(450,500) 
paper.add(mountain2)

mountain3 = mountain1.clone()
mountain3.moveTo(700,400)
paper.add(mountain3)

mountain4 = mountain1.clone()
mountain4.moveTo(950,500)
paper.add(mountain4)

#----Make the grass
grass = Rectangle(1000,200, Point(500,500))
grass.setFillColor("forestgreen")
grass.setBorderColor("forestgreen")
paper.add(grass)

#----Make tree leaves
tree = Ellipse(350,600,Point(80,150))
tree.setFillColor("seagreen")
tree.setBorderColor("springgreen4")
tree.setBorderWidth(10)
paper.add(tree)

#----Make tree trunk 
treetrunk = Rectangle(80,600,Point(40,300))
treetrunk.setFillColor("tan4")
treetrunk.setBorderColor("tan4")
paper.add(treetrunk)

#----Make tree hole
treehole = Circle(30,Point(0,500))
paper.add(treehole)

#----Make top tree branch 
treebranch1 = Rectangle(140,10, Point(100,150))
treebranch1.setFillColor("tan4")
treebranch1.setBorderColor("tan4")
paper.add(treebranch1)

#----Make bottom tree branch
treebranch1.rotate(-45)
treebranch2 = treebranch1.clone()
treebranch2.scale(1.3)
treebranch2.moveTo(120,250)
paper.add(treebranch2)

#----Make tree hole
treehole1 = Circle(30,Point(0,500))
paper.add(treehole1)

treehole2 = Circle(20, Point(0,500))
paper.add(treehole2)

treehole3 = Circle (10, Point(0,500))
paper.add(treehole3)

#----Make the man's head
head1 = Circle(15, Point(500,300))
head1.setFillColor("beige")
paper.add(head1)

#----Make the man's body
body1 = Rectangle(30,60,Point(500,345))
body1.setFillColor("black")
paper.add(body1)

#----Make the man's left arm 
arm11 = Path (Point(485,330),Point(470,315))
paper.add(arm11)

#----Make the man's right arm
arm12 = Path (Point (515,330), Point (530,345))
paper.add(arm12)

#----Make the man's left leg
leg11 = Path (Point (490,375), Point(490,400))
paper.add(leg11)

#----Make the man's right leg
leg12 = Path(Point(510,375), Point(510,400))
paper.add(leg12)

#----Make the man's left eye
eye11 = Circle(1,Point(493,293))
eye11.setFillColor("black")
paper.add(eye11)

#----Make the man's right eye
eye12 = Circle(1,Point(507,293))
eye12.setFillColor("black")
paper.add(eye12)

#----Make the man's mouth
mouth1 = Rectangle(10,5, Point(500,307))
mouth1.setFillColor("darkred")
paper.add(mouth1)

#----Make the tent
camp = Polygon(Point(900,450),Point(600,450),Point(750,250))
camp.setFillColor("orange")
paper.add(camp)
camp.setBorderWidth(4)

#----Make the tent's door
campDoor = Rectangle(60,80,Point(750,410))
campDoor.setFillColor("brown")
paper.add(campDoor)

campDoorLine = Path(Point(750,370),Point(750,450))
paper.add(campDoorLine)

#----Make the moon 
moon = Circle(50, Point(900,100))
moon.setFillColor("yellow")
paper.add(moon)

moonblocker = Circle(50,Point(860,100))
moonblocker.setFillColor("blue1")
moonblocker.setBorderColor("blue1")
paper.add(moonblocker)

#----Make textbackground
textback = Ellipse(215,56,Point(497,228))
textback.setFillColor("white")
paper.add(textback)

textcircle = Circle(5, Point(544,273))
textcircle.setFillColor("white")
paper.add(textcircle)

textcircle2 = textcircle.clone()
textcircle.moveTo(530,290)
paper.add(textcircle2)

#----Insert the text
text = Text("OMG, there is a giant monkey!")
text.moveTo(500,230)
paper.add(text)

#----Make firewood
firewood = Rectangle(80,20,Point(340,525))
firewood.setFillColor("chocolate4")
firewood.setBorderColor("chocolate4")
paper.add(firewood)

#----Make fire
fire1 = Circle(40,Point(340,475))
fire1.setFillColor("red2")
fire1.setBorderColor("red2")
paper.add(fire1)

fireblocker = Rectangle(80,40, Point(340,450))
fireblocker.setFillColor("forestgreen")
fireblocker.setBorderColor("forestgreen")
paper.add(fireblocker)

topfire = Polygon(Point(300,480),Point(313,435),Point(324,467),
Point(338,435),Point(343,467),Point(372,437),Point(380,480))
topfire.setFillColor("red2")
topfire.setBorderColor("red2")
paper.add(topfire)

#----Make stars
star1 = Polygon(Point(379,63), Point(380,80),Point(394,82),
Point(383,90),Point(385,107),Point(375,95),Point(358,103),
Point(367,87),Point(354,76),Point(373,78))
star1.setFillColor("yellow")
paper.add(star1)

star2 = star1.clone()
star2.moveTo(500,100)

paper.add(star2)

star3 = star2.clone()
star3.moveTo(684,81)
paper.add(star3)

star4 = star3.clone()
star4.moveTo(300,131)
star4.scale(0.5)
paper.add(star4)

star5 = star4.clone()
star5.moveTo(400,160)
star5.scale(1.3)
paper.add(star5)

#----Insert the monkey
monkey = Image("monkey2.gif")
monkey.moveTo(146,232)
paper.add(monkey)

#----The end.