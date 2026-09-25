### Works Cited
### 1.3.3 Monoliths

water = Rect(0,300,400,100,fill='lightBlue')

### buildings
buildingList = ['Bakery','Florist','Bank','Hotel','Boutique','Apartment']
app.anybuildings = False
app.anyRoad = False
app.anyfence = False
allBuildings = Group()
allBuildings.dx=0

def chooseColor():
    r = randrange(240,256)
    g = randrange(228,256)
    b = randrange(215,256)
    color = rgb(r,g,b)
    return color

def chooseBuilding():
    index = randrange(0,len(buildingList))
    building = buildingList[index]
    return building

### road and railings
road = Group()
road.dx=0

def drawRailingGroup(newX):
    app.url = 'cmu://1072811/48463264/stoneRoad_CMU.jpg'
    cobblestone = Image(app.url,newX,240)
    road.add(cobblestone)
    cobblestone.width=205
    cobblestone.height=60
    for i in range(newX,newX+200,50):
        road.add(
        Line(i,260,i,300,fill='white',lineWidth=10),
        Line(newX-5,270,newX+200,270,lineWidth=5))
        
def drawRR():
    
    if (app.anyRoad==False):
        newX = 0
        app.anyRoad = True
    else:
        newX = road.right
    
    drawRailingGroup(newX)

### exterior components

def drawWindowAndSign(windowSize,newX,newBuilding,base,signColor,label,font):
    
    if (windowSize == 1):
        ## window
        width = rounded(base.width-40)
        newBuilding.add(
        Rect(newX+20,20,width,30,fill='azure',border='white'),
        Line(newX+63,20,newX+63,50,fill='white'),
        Line(newX+103,20,newX+106,50,fill='white'),
        ## sign
        Rect(newX+15,55,base.width-30,35,fill=signColor),
        Label(label,newX+base.width/2,75,size=30,font=font),
        ## window
        Rect(newX+20,95,width,30,fill='azure',border='white'),
        Line(newX+63,95,newX+63,125,fill='white'),
        Line(newX+103,95,newX+106,125,fill='white'))
        
    elif (windowSize == 2):
        ## window grid
        for x in range(newX+15,newX+base.width-25,38):
            for y in range(15,126,50):
                newBuilding.add(Rect(x,y,25,30,fill='azure',border='white'))
        ## hotel sign
        if (base.fill=='aliceBlue'):
            newBuilding.add(
            Rect(newX+90,160,75,40,fill=signColor),
            Label(label,newX+127,180,size=25,font=font))

    elif (windowSize == 3):
        ## semicircle window
        x = newX + base.width/2
        width = base.width-40
        newBuilding.add(
            Arc(x,70,width,95,270,180,fill='azure',border='white'),
            Arc(x,100,width,95,90,180,fill='azure',border='white'),
            Line(x,70,x,30,fill='white'),
            Line(x,100,x,140,fill='white')
            )
        ## florist front
        # sign
        if (base.fill=='honeydew'):
            newBuilding.add(
            Oval(newX+100,180,75,40,fill=signColor),
            Label(label,newX+100,180,size=17,font=font))
        # flowers
            image2 = 'cmu://1072811/48689794/Screenshot+2026-09-24+at+11.29.37 AM.png'
            flowerBox1 = Image(image2,newX+30,70)
            flowerBox2 = Image(image2,newX+80,70)
            newBuilding.add(flowerBox1,flowerBox2)
            flowerBox1.width=40
            flowerBox1.height=30
            flowerBox2.width=40
            flowerBox2.height=30
            flowerBox1.opacity=65
            flowerBox2.opacity=65
        
def drawBuilding(wallColor, doorColor, windowSize, signColor, width, doubleDoor,label,font):
    
    ## check if theres any buildings and build the first one
    if (app.anybuildings==False):
        newX = 0
        app.anybuildings = True
    ## if there is, add onto the last building
    else:
        newX = allBuildings.right
        
    newBuilding = Group()
    allBuildings.add(newBuilding)
    ## wall
    base = Rect(newX,0,width,240,fill=wallColor,border='white')
    newBuilding.add(base)
    ## door
    newBuilding.add(
    Rect(newX+15,160,35,80,fill=doorColor,border='white'),
    Circle(newX+46,200,3,fill='darkGoldenRod'))
    if (doubleDoor==True):
        newBuilding.add(
        Rect(newX+50,160,35,80,fill=doorColor,border='white'),
        Circle(newX+54,200,3,fill='darkGoldenRod'))
    ## windows
    drawWindowAndSign(windowSize,newX,newBuilding,base,signColor,label,font)
    
def main():
    if (allBuildings.right<=450):
        ## bakery
        if (chooseBuilding()=='Bakery'):
            label = 'Bakery'
            wallColor = app.data['Bakery'][0]
            doorColor = app.data['Bakery'][1]
            windowSize = app.data['Bakery'][2]
            signColor = app.data['Bakery'][3]
            width = app.data['Bakery'][4]
            doubleDoor = app.data['Bakery'][5]
            font = app.data['Bakery'][6]
            drawBuilding(wallColor,doorColor,windowSize,signColor,width,doubleDoor,label,font)
        ## florist
        if (chooseBuilding()=='Florist'):
            label = 'Florist'
            wallColor = app.data['Florist'][0]
            doorColor = app.data['Florist'][1]
            windowSize = app.data['Florist'][2]
            signColor = app.data['Florist'][3]
            width = app.data['Florist'][4]
            doubleDoor = app.data['Florist'][5]
            font = app.data['Florist'][6]
            drawBuilding(wallColor,doorColor,windowSize,signColor,width,doubleDoor,label,font)
        ## bank
        if (chooseBuilding()=='Bank'):
            label = 'Bank'
            wallColor = app.data['Bank'][0]
            doorColor = app.data['Bank'][1]
            windowSize = app.data['Bank'][2]
            signColor = app.data['Bank'][3]
            width = app.data['Bank'][4]
            doubleDoor = app.data['Bank'][5]
            font = app.data['Bank'][6]
            drawBuilding(wallColor,doorColor,windowSize,signColor,width,doubleDoor,label,font)
        ## hotel
        if (chooseBuilding()=='Hotel'):
            label = 'Hotel'
            wallColor = app.data['Hotel'][0]
            doorColor = app.data['Hotel'][1]
            windowSize = app.data['Hotel'][2]
            signColor = app.data['Hotel'][3]
            width = app.data['Hotel'][4]
            doubleDoor = app.data['Hotel'][5]
            font = app.data['Bank'][6]
            drawBuilding(wallColor,doorColor,windowSize,signColor,width,doubleDoor,label,font)
        ## boutique
        if (chooseBuilding()=='Boutique'):
            label = 'Boutique'
            wallColor = app.data['Boutique'][0]
            doorColor = app.data['Boutique'][1]
            windowSize = app.data['Boutique'][2]
            signColor = app.data['Boutique'][3]
            width = app.data['Boutique'][4]
            doubleDoor = app.data['Boutique'][5]
            font = app.data['Boutique'][6]
            drawBuilding(wallColor,doorColor,windowSize,signColor,width,doubleDoor,label,font)
        ## apartment
        if (chooseBuilding()=='Apartment'):
            label = None
            wallColor = chooseColor()
            doorColor = app.data['Apartment'][1]
            windowSize = app.data['Apartment'][2]
            signColor = app.data['Apartment'][3]
            width = app.data['Apartment'][4]
            doubleDoor = app.data['Apartment'][5]
            font = app.data['Apartment'][6]
            drawBuilding(wallColor,doorColor,windowSize,signColor,width,doubleDoor,label,font)
        
def buildingMove():
    ## move buildings
    allBuildings.centerX+=allBuildings.dx
    allBuildings.dx=-2
    for building in allBuildings.children:
        if (building.right<=0):
            allBuildings.remove(building)
    
    ## move roads + fence
    road.centerX+=road.dx
    road.dx=-2
    for path in road.children:
        if (path.right<=0):
            road.remove(path)
            

    
            
# key : [wallColor, doorColor, windowSize(1, 2, or 3), signColor, width, doubleDoor, font]
app.data = {
    'Bakery': ['lavenderBlush', 'white', 3, 'white', 160, False, 'sacramento'],
    'Florist': ['honeydew', 'white', 3, 'lavenderBlush', 150, False, 'cinzel'],
    'Bank': ['antiqueWhite', 'tan', 1, 'tan', 165, True, 'montserrat'],
    'Hotel': ['aliceBlue', 'white', 2, 'white', 170, True, 'grenze'],
    'Boutique': ['mistyRose', 'white', 1, 'white', 155, False, 'caveat'],
    'Apartment' : [chooseColor(),'white',2,'white',131, False, None]
}


def onStep():
    for building in allBuildings.children:
        if (building.right<=0):
            allBuildings.remove(building)
    main()
    if (road.right<=600):
        drawRR()
  
    
    buildingMove()
    

Label('In Progress...',200,350,size=50,font='sacramento')
    




