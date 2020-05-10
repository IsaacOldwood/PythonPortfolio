#A script created for my show reselling buisness. No longer works so adding it to my portfolio
import requests
from bs4 import BeautifulSoup
import pause
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import string
import random
#driver=webdriver.Chrome()
#driver.get('https://www.bstn.com/en')

full_prodyct_url='https://www.bstn.com/en/p/nike-air-max-1-premium-875844-007-79031'
product_size='10_395'
amount_Ordered='1'
maxTries=10

#Make Cookies
cfdiud_cookie=''.join(random.choices(string.ascii_lowercase + string.digits, k=44))
ebusiness_shop_cookie=''.join(random.choices(string.ascii_lowercase + string.digits, k=25))

#Ping Website
headers1={
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
 'Cookie': f'__cfduid={cfdiud_cookie}; 3mo_ebusiness_shop_v3={ebusiness_shop_cookie}; bstnhome=men; cookieconsent_status=dismiss',
}
#Ping Website
r=requests.get("https://www.bstn.com/en",headers=headers1)
print(r)

#Navigate to product page
r=requests.get(full_prodyct_url,headers=headers1)
print(r)

#Get IDs
payload={
'chosen_attribute_value': product_size,
'returnHtmlSnippets[partials][0][module]': 'product',
'returnHtmlSnippets[partials][0][partialName]': 'buybox',
'returnHtmlSnippets[partials][0][path]': '_productDetail'
}
r=requests.post(full_prodyct_url,data=payload,headers=headers1)
print(r)
json=r.json()
product_ID=json['initializedProduct']['id']
product_BS_ID=json['initializedProduct']['bsId']

#ATC
atc_URL=f"https://www.bstn.com/en/cart/add?product_id={product_ID}&product_bs_id={product_BS_ID}&amount={amount_Ordered}&ajax=true&redirectRooting=&addToCart=&returnHtmlSnippets[partials][0][module]=cart&returnHtmlSnippets[partials][0][partialName]=cartHeader&returnHtmlSnippets[partials][0][returnName]=headerCartDesktop&returnHtmlSnippets[partials][0][params][template]=Standard&returnHtmlSnippets[partials][1][module]=cart&returnHtmlSnippets[partials][1][partialName]=cartHeader&returnHtmlSnippets[partials][1][returnName]=cartErrors&returnHtmlSnippets[partials][1][params][template]=errorMessage&returnHtmlSnippets[partials][2][module]=cart&returnHtmlSnippets[partials][2][partialName]=cartHeader&returnHtmlSnippets[partials][2][returnName]=headerCartMobile&returnHtmlSnippets[partials][2][params][template]=mobileNavbar&returnHtmlSnippets[partials][3][module]=product&returnHtmlSnippets[partials][3][path]=_productDetail&returnHtmlSnippets[partials][3][partialName]=buybox&returnHtmlSnippets[partials][3][returnName]=buybox&returnHtmlSnippets[partials][3][params][bsId]={product_BS_ID}"
for i in range(maxTries):
    r=requests.get(atc_URL,headers=headers1)
    if r.status_code==200:
        print("ATC Request Success!")
        break
    else:
        print("ATC Request Failed, Retrying...")
        pause.milliseconds(500)
    if i == maxTries:
     print('Max Tries Reached... Exiting Bot')
     sys.exit()


#Navigate to cart page to check previous 
r=requests.get("https://www.bstn.com/en/cart",headers=headers1)
soup=BeautifulSoup(r.text, "lxml")
print(r)
chosen_make=soup.body.find("h4").findAll("span")[0].next
chosen_name=soup.body.find("h4").findAll("span")[1].next
chosen_size=soup.body.find(attrs={"class":"atrributes"}).next
cart_Quantity=soup.body.find("select").find(attrs={'selected':""}).next
print('')
print(f'Cart: {chosen_make} {chosen_name}')
print(f'Quantity: {cart_Quantity}')
print(f'Size: {chosen_size}')
print('')

#Post Address Details
payload={
 'back_x_value': '@cart',
 'billaddress[addition]': '',
 'billaddress[city]': 'fgbh',
 'billaddress[country]': '10',
 'billaddress[forename]': 'bstn',
 'billaddress[lastname]': 'bot',
 'billaddress[phone]': '',
 'billaddress[salutation]':	'1',
 'billaddress[street_number]': 'cvbh',
 'billaddress[street]': 'fghj',
 'billaddress[zipcode]': 'AA111AA',
 'billAddressId': '-1',
 'guestdata[email_repeat]':	'a@gmail.com',
 'guestdata[email]': 'a@gmail.com',
 'next_x': 'Continue+to+payment',
 'next_x_value': '@cart_payment',
 'shippingaddress[addition]': '',
 'shippingaddress[city]': '',
 'shippingaddress[country]': '10',
 'shippingaddress[forename]': '',
 'shippingaddress[lastname]': '',
 'shippingaddress[salutation]': '',
 'shippingaddress[street_number]': '',
 'shippingaddress[street]': '',
 'shippingaddress[zipcode]': '',
 'shippingAddressId': '-1'
}

r=requests.post("https://www.bstn.com/en/cart/payment",data=payload,headers=headers1,allow_redirects=False)
print(r)

#Check Payment and Delivery Options
r=requests.get("https://www.bstn.com/en/cart/payment",headers=headers1)
print(r)
soup=BeautifulSoup(r.text,"lxml")
print(soup.body.find("h2").next.next)
shipping_method_value=soup.body.find(attrs={"name":"shipping_method_id"})['value']
print(shipping_method_value)


#driver.add_cookie({'name':'3mo_ebusiness_shop_v3','value':ebusiness_shop_cookie})
#driver.get('https://www.bstn.com/en/cart/payment')

#Post Payment Choice
payload={
 'back_x_value': '@cart_address',
 'next_x': 'Continue+to+summary',
 'next_x_value': '@cart_check',
 'payment_method_id': '6',
 'shipping_method_id': f'{shipping_method_value}'
}


r=requests.post("https://www.bstn.com/en/cart/check",data=payload,headers=headers1,allow_redirects=False)
print(r)
print(r.history)
for r in r.history:
    print(r.url)
soup=BeautifulSoup(r.text,"lxml")
print(soup)

r=requests.get("https://www.bstn.com/en/cart/check",headers=headers1)
print(r)
soup=BeautifulSoup(r.text,"lxml")
print(soup.body.find("h1"))

#print(f'__cfduid={cfdiud_cookie}; 3mo_ebusiness_shop_v3={ebusiness_shop_cookie}; bstnhome=men; cookieconsent_status=dismiss')

