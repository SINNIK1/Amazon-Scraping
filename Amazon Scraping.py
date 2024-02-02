#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[12]:


URL = 'https://www.amazon.in/Timex-Analog-Black-Dial-Watch-TW000R438/dp/B083JXS2YT/ref=sr_1_25?keywords=timex&sr=8-25'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65bccdf6-2ce966b17c1a8e8460497bb0"}
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(class_=['a-price-whole']).get_text()

print(title)
print(price)


# In[25]:


title = title.strip()
price = price.strip()

print(title)
print(price)


# In[31]:


import datetime 
today = datetime.date.today()

print(today)


# In[32]:


import csv

header = ['Title' , 'Price' , 'Date']
data = [title , price , today]

with open('AmazonWebScraperDataset.csv' , 'w' , newline='' , encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    


# In[36]:


import pandas as pd

df = pd.read_csv(r'C:\Users\k9811\AmazonWebScraperDataset.csv')

print(df)


# In[35]:


with open('AmazonWebScraperDataset.csv' , 'a+' , newline='' , encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[37]:


def check_price():
    URL = 'https://www.amazon.in/Timex-Analog-Black-Dial-Watch-TW000R438/dp/B083JXS2YT/ref=sr_1_25?keywords=timex&sr=8-25'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65bccdf6-2ce966b17c1a8e8460497bb0"}
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(class_=['a-price-whole']).get_text()
        
    title = title.strip()
    price = price.strip()
    
    import datetime 
    
    today = datetime.date.today()

    print(today)
    
    import csv

    header = ['Title' , 'Price' , 'Date']
    data = [title , price , today]
    
    with open('AmazonWebScraperDataset.csv' , 'a+' , newline='' , encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if(price<1801):
        send_mail()


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[40]:


import pandas as pd

df = pd.read_csv(r'C:\Users\k9811\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('kartik190302@gmail.com','poonam1075')
    
    subject = "The Watch you want is below 1800Rs! Now is your chance to buy!"
    body = "Kartik, This is the moment we have been waiting for. Now is your chance to pick up the Watch of your dreams. Don't mess it up! Link here: "https://www.amazon.in/Timex-Analog-Black-Dial-Watch-TW000R438/dp/B083JXS2YT/ref=sr_1_25?keywords=timex&sr=8-25" 
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'kartik190302@gmail.com',
        msg
     
    )


# In[ ]:





# In[ ]:




