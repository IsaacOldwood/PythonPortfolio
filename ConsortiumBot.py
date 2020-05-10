#This is a script I developed as part of my shoe reselling business. It no longer works due to site changes so I am happy to make it public as part of my portfolio

import requests
from bs4 import BeautifulSoup
import re
import uuid
import time
from datetime import datetime
import pause
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
import os
CWD=os.getcwd()
config = configparser.ConfigParser()

#Set Up Reading of Config File
config.read(r'\Config.ini')
config.sections()

#Proxies
proxy_user=config['Proxies']['proxy_user']
proxy_pass=config['Proxies']['proxy_pass']
proxy_ip=config['Proxies']['proxy_ip']
proxy_port=config['Proxies']['proxy_port']
proxie = {'http': f'http://{proxy_user}:{proxy_pass}@{proxy_ip}:{proxy_port}/'}
PROXY=f'{proxy_ip}:{proxy_port}'

#Variables
full_product_url=config['Shoe']['full_product_url']
shoe_size=config['Shoe']['shoe_size']
email_address=config['Billing']['email_address']
billing_city=config['Billing']['billing_city']
billing_country_id=config['Billing']['billing_country_id']
billing_first_name=config['Billing']['billing_first_name']
billing_last_name=config['Billing']['billing_last_name']
billing_post_code=config['Billing']['billing_post_code']
billing_region=config['Billing']['billing_region']
billing_address_line_1=config['Billing']['billing_address_line_1']
billing_address_line_2=config['Billing']['billing_address_line_2']
billing_telephone=config['Billing']['billing_telephone']
card_first_name=config['CardDetails']['card_first_name']
card_number=config['CardDetails']['card_number']
card_surname=config['CardDetails']['card_surname']
card_expiry_month=config['CardDetails']['card_expiry_month']
card_expiry_year=config['CardDetails']['card_expiry_year']
card_security_code=config['CardDetails']['card_security_code']
unixtimestamp=int(config['DropTime']['unixtimestamp']) #Set to drop

#Driver settings
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome(chrome_options=chrome_options)

#Shoe Variables
formkey = f'{uuid.uuid4}'
r= requests.get(full_product_url,proxies=proxie)
soup=BeautifulSoup(r.text,"lxml")
product_id=soup.body.find("span",class_="regular-price")['id'][-5:]
print('')
print(f'{datetime.now().time()}-Variables Parsed')

#Solve captcha
driver.get('http://www.consortium.co.uk/checkout/cart/')
driver.get(full_product_url)
pause.milliseconds(50)
frontend_cookie=driver.get_cookie('frontend')['value']

headers={
    'Cookie': f'frontend={frontend_cookie}'
}
pause.until(unixtimestamp) #Pause until drop
start_time=time.time()
pause.milliseconds(5)
r = requests.get('http://www.consortium.co.uk/checkout/cart/',headers=headers,proxies=proxie)
soup = BeautifulSoup(r.text, "lxml")
basket_check=soup.body.find("h1").next.strip()

i=1
while i<1000:
    if basket_check=='Your Basket is Empty':
     pause.milliseconds(10)#Change this to shorter after testing
     r = requests.get('http://www.consortium.co.uk/checkout/cart/',headers=headers,proxies=proxie)
     soup = BeautifulSoup(r.text, "lxml")
     basket_check=soup.body.find("h1").next.strip()
     i=i+1
     continue
    else:
     driver.close()
     break

#Navigate to Cart Page
r = requests.get('http://www.consortium.co.uk/checkout/cart/',headers=headers,proxies=proxie)
soup = BeautifulSoup(r.text, "lxml")
#Used to debug: print(r)
#Used to debug: print(soup.body.findAll("h1"))
#Used to debug: print('')
name_of_item_in_cart=soup.body.findAll("span",class_="cart-product-title")[0].next.strip()
cart_total=soup.body.find("strong",text=re.compile('Grand Total Incl. VAT')).parent.parent.find("span",class_="price").next.strip()
print('')
print(f'Item in cart: {name_of_item_in_cart[4:]}')
print(f'Quantity: {name_of_item_in_cart[:1]}')
print(f'Cart Total: {cart_total}')
print('')
print(f'{datetime.now().time()}-Checkout Page')

#Go to next page
headers1={
    'Cookie': f'frontend={frontend_cookie}'
}

r=requests.get('https://www.consortium.co.uk/checkout/secure/login/',headers=headers1,proxies=proxie)

soup = BeautifulSoup(r.text, "lxml")
#Used to debug: print(soup.body.findAll("h2",text=re.compile('Checkout')))
frontend_cid_cookie=r.headers['set-cookie'][13:29]
#Used to debug: print('')



#Input Email

headers2={
    'Cookie': f'frontend={frontend_cookie};frontend_cid={frontend_cid_cookie}'
}

payload= {
    'register[email]': email_address
}
r = requests.post('https://www.consortium.co.uk/checkout/secure/registerPost/',data=payload,headers=headers2,allow_redirects=False,proxies=proxie)
r = requests.post('https://www.consortium.co.uk/checkout/secure/billing/',data=payload,headers=headers2,allow_redirects=False,proxies=proxie)
#Used to debug: print(r)
print(f'{datetime.now().time()}-Email Added')
#Used to debug: print(soup.body.findAll("span",text=re.compile('Billing')))
#Used to debug: print(soup.body.findAll("input",id='billing:email'))
#Used to debug: print(f'Cart: {soup.body.findAll("span",class_="cart-product-title")[0].next.strip()}')

#Billing Info

payload= {
 'billing[address_id]': '1261868',
 'billing[city]': billing_city,	
 'billing[country_id]':	billing_country_id,
 'billing[email]': email_address,
 'billing[firstname]':	billing_first_name,
 'billing[lastname]':	billing_last_name,
 'billing[postcode]':	billing_post_code,
 'billing[region]':	billing_region,
 'billing[save_in_address_book]': '1',
 'billing[street][0]': billing_address_line_1,
 'billing[street][1]': billing_address_line_2,
 'billing[telephone]':	billing_telephone,
 'billing[use_for_shipping]': '1'
}
r = requests.post('https://www.consortium.co.uk/checkout/secure/billingPost/',data=payload,headers=headers2,allow_redirects=False,proxies=proxie)
r = requests.post('https://www.consortium.co.uk/checkout/secure/shippingmethod/',data=payload,headers=headers2,allow_redirects=False,proxies=proxie)
#Used to debug: print(r)
print(f'{datetime.now().time()}-Billing info added')
soup = BeautifulSoup(r.text, "lxml")
#Used to debug: print(soup.body.findAll("span",text=re.compile('Shipping')))
#Used to debug: print(f'Cart: {soup.body.findAll("span",class_="cart-product-title")[0].next.strip()}')

#Pick Shipping

payload= {
    'shipping_method':'freeshipping_freeshipping'
}
r = requests.post('https://www.consortium.co.uk/checkout/secure/shippingMethodPost/',data=payload,headers=headers2,allow_redirects=False,proxies=proxie)
r = requests.post('https://www.consortium.co.uk/checkout/secure/payment/',data=payload,headers=headers2,allow_redirects=False,proxies=proxie)
#Used to debug: print(r)
soup = BeautifulSoup(r.text, "lxml")
#Used to debug: print(soup.body.findAll("span",text=re.compile('Payment')))
chosen_shipping=soup.body.findAll("h3",text=re.compile('Shipping Method'))[0].parent.find("p").next.strip()
print(f'Chosen Shipping: {chosen_shipping}')
print(f'Cart: {soup.body.findAll("span",class_="cart-product-title")[0].next.strip()}')
print(f'{datetime.now().time()}-Shipping Chosen')



payload= {
    'payment[method]':'sagepayserver'
}

r = requests.post(f'https://www.consortium.co.uk/sgps/payment/onepageSaveOrder/?SID={frontend_cookie}',data=payload,headers=headers2,allow_redirects=False,proxies=proxie)
json = r.json()
vpstxid=json['v_ps_tx_id']
#Used to debug: print(vpstxid)


r = requests.get(f'https://live.sagepay.com/gateway/service/cardselection?vpstxid={vpstxid}',allow_redirects=False,proxies=proxie)
#Used to debug: print(r)
jsessionid_cookie=r.headers['set-cookie'][11:43]
NSC_cookie=r.headers['set-cookie'][101:173]


headers3={
    'Cookie': f'JSESSIONID={jsessionid_cookie}; NSC_WJQ-mjwf.tbhfqbz.dpn-Hbufxbz={NSC_cookie}'
}

r = requests.get(f'https://live.sagepay.com/gateway/service/carddetails;jsessionid={jsessionid_cookie}',headers=headers3,proxies=proxie)
#Used to debug: print(r)
soup = BeautifulSoup(r.text, "lxml")
#Used to debug: print(soup.body.findAll("input",{"name":"cardfirstnames"}))
#Correct up to here
#Post card details

headers4={
    'Cookie': f'JSESSIONID={jsessionid_cookie}; NSC_WJQ-mjwf.tbhfqbz.dpn-Hbufxbz={NSC_cookie}'
}

payload={
 'action': 'proceed',
 'cardfirstnames': card_first_name,
 'cardnumber': card_number,
 'cardsurname': card_surname,
 'clickedButton': 'proceed',
 'expirymonth': card_expiry_month,
 'expiryyear': card_expiry_year,
 'securitycode': card_security_code
}

r=requests.post('https://live.sagepay.com/gateway/service/carddetails',headers=headers4,data=payload,allow_redirects=False,proxies=proxie)
#Used to debug: print(r)
r=requests.get('https://live.sagepay.com/gateway/service/cardconfirmation',headers=headers4,allow_redirects=False,proxies=proxie)
#Used to debug: print(r)
r=requests.get('https://live.sagepay.com/gateway/service/authentication',headers=headers4,allow_redirects=False,proxies=proxie)
#Used to debug: print(r)
soup = BeautifulSoup(r.text, "lxml")
#Used to debug: print(soup.body.findAll("p"))
#Used to debug: print('')
paReq_cookie=soup.body.find("form").find("input")['value']
MD_cookie=soup.body.find("form").findAll("input")[2]['value']
print(f'{datetime.now().time()}-Card details added')


payload={
    'MD':f'{MD_cookie}',
    'PaReq':f'{paReq_cookie}',
    'TermUrl': f'https://live.sagepay.com/gateway/service/authentication;jsessionid={jsessionid_cookie}?action=completion'
}
r=requests.post('https://cap.attempts.securecode.com/acspage/cap?RID=136&VAA=A',data=payload,proxies=proxie)
#Used to debug: print(r)
soup = BeautifulSoup(r.text, "lxml")
paRes_cookie=soup.body.findAll("input")[2]['value']

payload={
    'ABSlog': 'GPP',	
    'isDNADone': 'false',
    'MD':f'{MD_cookie}',	
    'mescIterationCount': '0',
    'PaReq': f'{paReq_cookie}',
    'PaRes': f'{paRes_cookie}'
}
r=requests.post(f'https://live.sagepay.com/gateway/service/authentication;jsessionid={jsessionid_cookie}?action=completion',headers=headers4,data=payload,allow_redirects=False,proxies=proxie)
#Used to debug: print(r)
r=requests.post('https://live.sagepay.com/gateway/service/authorisation',headers=headers4,data=payload,allow_redirects=False,proxies=proxie)
#Used to debug: print(r)
print(f'{datetime.now().time()}-Purchase successful')
end_time=time.time()
print(f'Elapsed time: {end_time-start_time}')
