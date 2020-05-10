#All Scripts Assume birdsEye View


def dropAll():
    import pyautogui as pag 

    #Dropping All
    pag.keyDown('shift')

    #Row 1
    pag.moveTo(1774,766,1)
    pag.click()

    pag.moveTo(1820,766,0.2)
    pag.click()

    pag.moveTo(1862,766,0.2)
    pag.click()

    #Row 2
    pag.moveTo(1736,801,0.37)
    pag.click()

    pag.moveTo(1776,801,0.2)
    pag.click()

    pag.moveTo(1817,801,0.2)
    pag.click()

    pag.moveTo(1858,801,0.2)
    pag.click()

    #Row 3
    pag.moveTo(1736,835,0.37)
    pag.click()

    pag.moveTo(1776,835,0.2)
    pag.click()

    pag.moveTo(1817,835,0.2)
    pag.click()

    pag.moveTo(1858,835,0.2)
    pag.click()

    #Row 4
    pag.moveTo(1736,872,0.37)
    pag.click()

    pag.moveTo(1776,872,0.2)
    pag.click()

    pag.moveTo(1817,872,0.2)
    pag.click()

    pag.moveTo(1858,872,0.2)
    pag.click()

    #Row 5
    pag.moveTo(1736,909,0.37)
    pag.click()

    pag.moveTo(1776,909,0.2)
    pag.click()

    pag.moveTo(1817,909,0.2)
    pag.click()

    pag.moveTo(1858,909,0.2)
    pag.click()

    #Row 6
    pag.moveTo(1736,944,0.37)
    pag.click()

    pag.moveTo(1776,944,0.2)
    pag.click()

    pag.moveTo(1817,944,0.2)
    pag.click()

    pag.moveTo(1858,944,0.2)
    pag.click()

    #Row 7
    pag.moveTo(1736,981,0.37)
    pag.click()

    pag.moveTo(1776,981,0.2)
    pag.click()

    pag.moveTo(1817,981,0.2)
    pag.click()

    pag.moveTo(1858,981,0.2)
    pag.click()

    pag.keyUp('shift')

    return 1

def randomMouseMovements(seconds):
    import pyautogui as pag 
    import pause
    import random
    import math
    movements=math.ceil((int(seconds)/5))

    for _ in range(0,movements):
        pag.moveTo(random.randint(8,1903),random.randint(1,1027),2)
        pause.seconds(3)

    return 1

def clickTile(direction):
    import pyautogui as pag 

    if direction.lower() == 'd':
        pag.moveTo(969,656,1)
    elif direction.lower() == 'r':
        pag.moveTo(1069,615,1)
    pag.click()

    return 1

def changeWindow(number):
    import pyautogui as pag
    import pause

    if number == 8:
        pag.moveTo(371,1060)
    
    pag.click()
    pause.milliseconds(500)

    return 1

def selectGameNotifications():
    import pyautogui as pag
    pag.moveTo(99,1027,0.5)
    pag.click()
    return 1

def screenGrab(bbox=None):
    from PIL import ImageGrab

    return ImageGrab.grab(bbox)

def checkCopperOre(direction):
    import datetime
    s=screenGrab()
    if direction.lower() == 'd':
        pixels=[(985,609),(975,620),(991,631)]

    for pixel in pixels:

        if s.getpixel(pixel) != (107,70,38):
            print('Ore Not Avaliable')
            continue
        else:
            print(f'{datetime.datetime.now().time():%H-%M-%S} Ore Avliable')
            return pixel

    return 0

def checkIronOre(direction,k):
    import datetime
    #s=screenGrab(bbox=(888,569,1000,670))
    s=screenGrab()
    if direction.lower() == 'd':
        pixels=[(961,621),(962,602),(985,609),(975,620),(991,631)]

    for pixel in pixels:

        if s.getpixel(pixel) != (54,27,19):
            if k%6==0:
                print('Ore Not Avaliable')
            continue
        else:
            print(f'{datetime.datetime.now().time():%H:%M:%S} Ore Avliable')
            return pixel

    return 0

def checkFullInvetory():
    import datetime
    s=screenGrab()

    if s.getpixel((1858,981)) != (62,53,41):
        print(f'{datetime.datetime.now().time():%H:%M:%S} Inventory Full')
        return 1
    else:
        print(f'{datetime.datetime.now().time():%H:%M:%S} Inventory Not Full')
        return 0

def saveOutput():
    import sys
    orig_stdout = sys.stdout
    f = open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\RuneScape\OSRSBotOutput.txt','w')
    sys.stdout = f

    #Do Stuff

    sys.stdout = orig_stdout
    f.close()

def checkCopperMineSuccess():
    from PIL import Image
    import datetime
    s=screenGrab(bbox=(10,981,199,995))
    sucMsg=Image.open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\RuneScape\CopperMineSuccess.png')

    pairs = zip(sucMsg.getdata(),s.getdata())

    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    if dif == 0:
        print(f'{datetime.datetime.now().time():%H-%M-%S} Mining Finished')
        return 1
    else:
        print('Mining Not Finished')
        return 0

def checkIronMineSuccess():
    from PIL import Image
    import datetime
    s=screenGrab(bbox=(10,981,182,995))
    sucMsg=Image.open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\RuneScape\IronMineSuccess.png')

    pairs = zip(sucMsg.getdata(),s.getdata())

    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    if dif == 0:
        print(f'{datetime.datetime.now().time():%H:%M:%S} Mining Finished')
        return 1
    else:
        print('Mining Not Finished')
        return 0

def mineCopperBot():
    #Down at lumbridge bottom copper stood above
    import pause
    import pyautogui as  pag 
    import sys
    import datetime
    orig_stdout = sys.stdout
    f = open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\RuneScape\OSRSBotOutput.txt','w')
    sys.stdout = f
    
    print(f'{datetime.datetime.now():%Y-%m-%d}')
    changeWindow(8)
    selectGameNotifications()
    IS=checkFullInvetory()
    
    
    while IS==0:
        i=0
    
        oA=checkCopperOre('d')
        
        while oA==0:
            pause.seconds(1)
            oA=checkCopperOre('d')
        print(f'{datetime.datetime.now().time():%H-%M-%S} Mining...')
        
        pag.moveTo(oA[0],oA[1],0.5)
        pag.click()
        pause.milliseconds(1500)
    
        mS=checkCopperMineSuccess()
    
        while mS ==0:
            pause.milliseconds(500)
            mS=checkCopperMineSuccess()
            if i >= 24:
                break
            i+=1

    
        IS=checkFullInvetory()
        print(f'{datetime.datetime.now().time():%H-%M-%S} Checking Ore...')
    
    
    dropAll()
    
    sys.stdout = orig_stdout
    f.close()

    return 1

def varrockIronOreRun(numberOfRuns=1):
    #Start above iron ore in west mine, each rotation takes 5:30min
    import sys
    import pause
    import datetime
    import pyautogui as pag 
    orig_stdout = sys.stdout
    f = open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\RuneScape\OSRSBotOutput.txt','w')
    sys.stdout = f

    print(f'{datetime.datetime.now():%Y-%m-%d}')
    changeWindow(8)
    selectGameNotifications()

    for k in range(1,numberOfRuns+1):
        IS=checkFullInvetory()
    
        while IS==0:
            i=0
            l=1
        
            oA=checkIronOre('d',l)
            
            while oA==0:
                pause.milliseconds(100)
                oA=checkIronOre('d',l)
                l+=1
            print(f'{datetime.datetime.now().time():%H:%M:%S} Mining...')
            
            pag.moveTo(oA[0],oA[1],0.5)
            pag.click()
            pause.milliseconds(1500)
        
            mS=checkIronMineSuccess()
        
            while mS ==0:
                pause.milliseconds(500)
                mS=checkIronMineSuccess()
                if i >= 24:
                    break
                i+=1
    
        
            IS=checkFullInvetory()
            print(f'{datetime.datetime.now().time():%H:%M:%S} Checking Ore...')
    
        print(f'{datetime.datetime.now().time():%H:%M:%S} Finished Mining! Heading To Bank...')
        #Walk
        pag.moveTo(1819,40,0.4)
        pag.click()
        pause.seconds(12)
        pag.moveTo(1818,37,0.2)
        pag.click()
        pause.seconds(12)
        pag.moveTo(1840,37,0.2)
        pag.click()
        pause.seconds(12)
        pag.moveTo(1879,62,0.2)
        pag.click()
        pause.seconds(12)
        pag.moveTo(1304,517,0.4)
        pag.click()
        pause.seconds(3)
    
        #Deposit All
        pag.moveTo(1780,768,0.4)
        pag.click()
        pause.seconds(1)
        pag.moveTo(1061,65,0.4)
        pag.click()
        print(f'{datetime.datetime.now().time():%H:%M:%S} Deposited! Heading Back...')

        if k != numberOfRuns:

            #Walk Back
            pause.seconds(1)
            pag.moveTo(1780,153,0.4)
            pag.click()
            pause.seconds(13)
            pag.moveTo(1837,180,0.2)
            pag.click()
            pause.seconds(12)
            pag.click()
            pause.seconds(12)
            pag.moveTo(1864,156,0.2)
            pag.click()
            pause.seconds(10)
            pag.moveTo(1238,1030,0.4)
            pag.click()
            pause.seconds(10)

        print(f'{datetime.datetime.now().time():%H:%M:%S} Loop {k} Finished!')


    print(f'{datetime.datetime.now().time():%H:%M:%S} Finished Loops!')
    selectGameNotifications()
    sys.stdout = orig_stdout
    f.close()

def checkHealth():
    from PIL import Image
    import os

    s=screenGrab(bbox=(1716,84,1730,96))

    hpDir=r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\RuneScape\HPSGrabs'

    for f in os.listdir(hpDir):
        hpMsg=Image.open(os.path.join(hpDir,f))

        pairs = zip(hpMsg.getdata(),s.getdata())

        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

        if dif <= 2000:
            currentHP=int(f[:-6])
            return currentHP
        else:
            #s.save("HP.png","PNG")
            #print(dif)
            pass
    
    currentHP=1
    return currentHP

def afkComabt(maxHP,foodRegen=7):
    #Will check for food in your inventory and keep moving the mouse
    import random
    import pyautogui as pag 
    import datetime
    import sys
    import pause

    orig_stdout = sys.stdout
    f = open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\RuneScape\OSRSBotOutput.txt','w')
    sys.stdout = f
    
    print(f'{datetime.datetime.now():%Y-%m-%d}')

    now=datetime.datetime.now()

    nowPlus10=now+datetime.timedelta(minutes=10)

    changeWindow(8)

    currentHP=checkHealth()
    print(f'{datetime.datetime.now().time():%H:%M:%S} Current Health: {currentHP}')

    pixels=[(1774,766),(1820,766),(1862,766),(1736,801),(1776,801),(1817,801),(1858,801),(1736,835),(1776,835),(1817,835),(1858,835),(1736,872),(1776,872),(1817,872),(1858,872),(1736,909),(1776,909),(1817,909),(1858,909),(1736,944),(1776,944),(1817,944),(1858,944),(1738,981),(1776,981),(1817,981),(1858,981)]

    k=1

    

    while True:

        if currentHP<=(maxHP-foodRegen):
            s=screenGrab()
            foodEaten=False
            
            for pixel in pixels:

                if (s.getpixel(pixel) != (62,53,41)) and (s.getpixel(pixel) != (59,50,38)) and (s.getpixel(pixel) != (64,54,44)) :#Space not empty
                    #print(s.getpixel(pixel))
                    pag.moveTo(pixel[0],pixel[1],0.3)
                    pag.click() #Eat foods
                    print(f'{datetime.datetime.now().time():%H:%M:%S} Food Eaten')
                    pause.milliseconds(0.7)
                    currentHP=checkHealth()
                    print(f'{datetime.datetime.now().time():%H:%M:%S} Current Health: {currentHP}')
                    k=1
                    foodEaten=True

                    break
                else:
                    pass
                    
            if foodEaten==False:
                print(f'{datetime.datetime.now().time():%H:%M:%S} Out Of Food!')
                return 1
            elif datetime.datetime.now()==nowPlus10:
                print(f'{datetime.datetime.now().time():%H:%M:%S} Monsters Tolerant!')
                return 1

                


        else:
            pag.moveTo(random.randint(8,1903),random.randint(1,1027),0.33)
            pag.moveTo(random.randint(8,1903),random.randint(1,1027),0.33)
            pag.moveTo(random.randint(8,1903),random.randint(1,1027),0.33)
            pause.seconds(1)
            currentHP=checkHealth()
            k+=1
            if k%5==0:
                print(f'{datetime.datetime.now().time():%H:%M:%S} Current Health: {currentHP}')
            elif datetime.datetime.now()>=nowPlus10:
                print(f'{datetime.datetime.now().time():%H:%M:%S} Monsters Tolerant!')
                return 1


    sys.stdout = orig_stdout
    f.close()