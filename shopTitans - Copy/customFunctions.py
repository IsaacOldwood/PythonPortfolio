import pyautogui as pag
import pause
from PIL import Image
import sys
import os
import datetime
import json
import requests
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Isaac.LAPTOP-KA6VL0F5\AppData\Local\Tesseract-OCR\tesseract.exe'


def changeWindow(number):

    if number == 8:
        pag.moveTo(371,1060)
    elif number == 7:
        pag.moveTo(321,1064)
    
    pag.click()
    pause.milliseconds(500)

    return 1

def screenGrab(bbox=None):
    from PIL import ImageGrab

    return ImageGrab.grab(bbox)

def saveOutput():
    orig_stdout = sys.stdout
    f = open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\RuneScape\OSRSBotOutput.txt','w')
    sys.stdout = f

    #Do Stuff

    sys.stdout = orig_stdout
    f.close()

def getCoinPrices():
    s1=screenGrab(bbox=(22,332,322,499))
    #s1.save(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\NewPrice1.png',"PNG")
    
    s2=screenGrab(bbox=(22,502,322,669))
    #s2.save(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\NewPrice2.png',"PNG")
    
    s3=screenGrab(bbox=(322,332,622,499))
    #s3.save(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\NewPrice3.png',"PNG")

    s4=screenGrab(bbox=(322,502,622,669))
    #s3.save(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\NewPrice4.png',"PNG")

    s5=screenGrab(bbox=(622,332,922,499))
    #s3.save(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\NewPrice5.png',"PNG")

    s6=screenGrab(bbox=(622,502,922,669))
    #s3.save(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\NewPrice6.png',"PNG")

    return [s1, s2, s3, s4, s5, s6]

def refreshPrices():

    pag.moveTo(1134,241,0.1)
    pag.click()
    pause.milliseconds(500)
    pag.click()
    pause.milliseconds(3000)

    return 1

def oldCheckPrice(s):
    coinPriceDir=r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\coinPrices'
    newCoinPriceDir=r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\newCoinPrices'


    for f in os.listdir(coinPriceDir):
        coinImg=Image.open(os.path.join(coinPriceDir,f))

        pairs = zip(coinImg.getdata(),s.getdata())

        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
        #print(f)
        #print(dif)
        #print('')

        if dif <= 5000:
            if f[:-4] == '-':
                currentPrice=0
            else:
                currentPrice=int(f[:-4])
            return currentPrice
        else:
            pass
            
    for f in os.listdir(newCoinPriceDir):
                coinImg=Image.open(os.path.join(newCoinPriceDir,f))

                pairs = zip(coinImg.getdata(),s.getdata())
        
                dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

                if dif<= 5000:
                    currentPrice=0
                    return currentPrice
                else:
                    pass
    
    s.save(os.path.join(newCoinPriceDir,'newCoinPrice'+(str(len(os.listdir(newCoinPriceDir))+1))+'.png'),"PNG")
    currentPrice=0
    return currentPrice

def checkPrice(img):
    
    img = img.convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        if item[0] > 190 and item[1] > 190 and item[2] > 190:
            newData.append((0, 0, 0))
        elif item[0] < 190 or item[1] < 190 or item[2] < 190:
            newData.append((255, 255, 255))
        else:
            newData.append(item)
    
    img.putdata(newData)
    
    currentPrice=pytesseract.image_to_string(img, config='digits')

    if currentPrice=='':
        currentPrice="null"
    else:
        currentPrice=int(currentPrice)

    return currentPrice

def collectCoinPrices():
    changeWindow(7)

    while True:
    
        refreshPrices()
        
        coinPrices=getCoinPrices()
        
        for s in coinPrices:
        
            checkPrice(s)
            #print(price)
    
        pause.seconds(30)

    return 1

def updateSwordPrices():
    #Have tier 1 and 2 swords open in the market
    changeWindow(7)

    headers1={
        "content-Type":"application/json; charset=utf-8",
        "dataType":"json",
    }

    while True:
        refreshPrices()

        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\swords\tier1.json') as f:
            tier1=json.load(f)
    
        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\swords\tier2.json') as f:
            tier2=json.load(f)
    
        s=getCoinPrices()
    
        currentPrice1=checkPrice(s[0])
        currentPrice2=checkPrice(s[1])

        if currentPrice1==0:
            currentPrice1='null'

        if currentPrice2==0:
            currentPrice2='null'
    
        newPrice1=[int(datetime.datetime.now().timestamp())*1000,currentPrice1]
    
        newPrice2=[int(datetime.datetime.now().timestamp())*1000,currentPrice2]
    
        tier2['series'][0]['values'].append(newPrice1)
        tier1['series'][0]['values'].append(newPrice2)

        tier2['series'][0]['values']=tier2['series'][0]['values'][-15:]
        tier1['series'][0]['values']=tier1['series'][0]['values'][-15:]

        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\swords\tier1.json','w') as f:
            json.dump(tier1,f,indent=2)
    
        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\swords\tier2.json','w') as f:
            json.dump(tier2,f,indent=2)
        
        requests.put('https://jsonstorage.net/api/items/5efaf4ba-6b77-477b-8371-f7366b4afbe7',headers=headers1,data=str(tier1))

        requests.put('https://jsonstorage.net/api/items/e3450994-461c-4081-a1df-df1c4cf2013c',headers=headers1,data=str(tier2))

        pause.seconds(60)

def oldUpdateComponentsPrices():
    #Have tier 1-2 componenets open in the market
    changeWindow(7)

    headers1={
        "content-Type":"application/json; charset=utf-8",
        "dataType":"json",
    }

    while True:
        refreshPrices()

        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\components\webbedWing.json') as f:
            webbedWing=json.load(f)
        
        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\components\preciousGem.json') as f:
            preciousGem=json.load(f)

        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\components\silverDust.json') as f:
            silverDust=json.load(f)
    
        s=getCoinPrices()
    
        currentPrice1=checkPrice(s[0])
        currentPrice2=checkPrice(s[1])
        currentPrice3=checkPrice(s[2])
    
        newPrice1=[int(datetime.datetime.now().timestamp())*1000,currentPrice1]
        newPrice2=[int(datetime.datetime.now().timestamp())*1000,currentPrice2]
        newPrice3=[int(datetime.datetime.now().timestamp())*1000,currentPrice3]
    
        webbedWing['series'][0]['values'].append(newPrice3)
        preciousGem['series'][0]['values'].append(newPrice2)
        silverDust['series'][0]['values'].append(newPrice1)

        webbedWing['series'][0]['values']=webbedWing['series'][0]['values'][-15:]
        preciousGem['series'][0]['values']=preciousGem['series'][0]['values'][-15:]
        silverDust['series'][0]['values']=silverDust['series'][0]['values'][-15:]

        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\components\webbedWing.json','w') as f:
            json.dump(webbedWing,f,indent=2)

        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\components\preciousGem.json','w') as f:
            json.dump(preciousGem,f,indent=2)

        with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\components\silverDust.json','w') as f:
            json.dump(silverDust,f,indent=2)
        
        requests.put('https://jsonstorage.net/api/items/434cb077-e3b8-4c40-9c02-37c993f8b348',headers=headers1,data=str(webbedWing))
        requests.put('https://jsonstorage.net/api/items/4b1c2792-ce9f-468f-b1fc-6d7b5401db51',headers=headers1,data=str(preciousGem))
        requests.put('https://jsonstorage.net/api/items/181c3a07-9545-4a46-8a8a-745300eb0f65',headers=headers1,data=str(silverDust))

        pause.seconds(60)

def updateComponentsPrices():
    #Have tier 1-2 componenets open in the market
    changeWindow(7)

    componentsImageDir=r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\itemImages\components'

    headers1={
        "content-Type":"application/json; charset=utf-8",
        "dataType":"json",
    }

    while True:
        refreshPrices()

        allS=getCoinPrices()

        for s in allS:

            itemName=identifyItem(s.crop((99,8,200,109)),componentsImageDir)
            #print(itemName)
    
            with open(os.path.join(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\components',itemName+'.json')) as f:
                itemJson=json.load(f)
        
            currentPrice1=checkPrice(s.crop((11,118,149,147)))
        
            newPrice1=[int(datetime.datetime.now().timestamp())*1000,currentPrice1]
        
            itemJson['series'][0]['values'].append(newPrice1)
    
            itemJson['series'][0]['values']=itemJson['series'][0]['values'][-20:]
    
            with open(os.path.join(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\components',itemName+'.json'),'w') as f:
                json.dump(itemJson,f,indent=2)
        
            itemID=componentJsonID(itemName)

            requests.put('https://jsonstorage.net/api/items/'+itemID,headers=headers1,data=str(itemJson))

        pause.seconds(60)

def identifyItem(s,itemDir):
    
    for f in os.listdir(itemDir):
        coinImg=Image.open(os.path.join(itemDir,f))

        pairs = zip(coinImg.getdata(),s.getdata())

        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
        #print(f)
        #print(dif)
        #print('')

        if dif <= 5000:
            itemName=f[:-4]
            return itemName
        else:
            pass

    s.save('BadImage.png',"PNG")
    return 0

def componentJsonID(itemName):

    if itemName=='webbedWing':
        return '434cb077-e3b8-4c40-9c02-37c993f8b348'
    elif itemName=='preciousGem':
        return '4b1c2792-ce9f-468f-b1fc-6d7b5401db51'
    elif itemName=='silverDust':
        return '181c3a07-9545-4a46-8a8a-745300eb0f65'
    elif itemName=='elvenWood':
        return '225222be-6f57-487c-b964-0d9cf3836bb5'
    elif itemName=='ironPineCone':
        return 'b1659a25-8247-4082-9dd5-196c2a13b8ca'
    elif itemName=='glowShroom':
        return 'b516ba07-a652-4645-907e-cb2114a259cf'