# -*- coding: cp936 -*-
import urllib
from HTMLParser import HTMLParser
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
from email.mime.multipart import MIMEMultipart  
#crawl the page
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

html=getHtml("http://192.168.168.178/001")

#analysis the html

from selenium import webdriver
bagp=webdriver.Chrome()
bagp.get('http://192.168.1.178/001.html')
Pressureb=bagp.find_element_by_id('')
count=Pressure.find_eleent_by_class_name('')
count.text

# Alarm set
if   P>60:
   subject='the pressure in bag is too high'
    elif P<1:
    subject='the pessure in bag is too low'

 #send e-mail
 sender = '*******'
 receiver = '********'
 smtpserver = 'smtp.qq.com'  
 username = '********'
 password = '*******'
  
 msg =MIMEMultipart('related')  
 msg['Subject'] = Header(subject, 'utf-8')  
 
 att = MIMEText(open('E:\esdfree\emailtest.py', 'rb').read(), 'base64', 'utf-8')  
 att["Content-Type"] = 'application/octet-stream'  
 att["Content-Disposition"] = 'attachment; filename="emailtest.py"'  
 msg.attach(att)    
    
 smtp = smtplib.SMTP()  
 smtp.connect('smtp.qq.com')
 smtp.ehlo()  
 smtp.starttls()  
 smtp.ehlo()  
 smtp.login(username, password)  
 smtp.sendmail(sender, receiver, msg.as_string())  
 smtp.quit()  
