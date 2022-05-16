import requests,random,sys,os
from hashlib import sha256
#--------------------------------------------------------------------
from bs4 import BeautifulSoup as BS
#--------------------------------------------------------------------
url2 = "https://services.orange.eg/GetToken.svc/GenerateToken"
#---------------------------------------------------------------------
hd2 = {  "Content-Type":"application/json; charset=UTF-8", 
  "Content-Length":"78" , 
  "Host":"services.orange.eg"
   , "Connection":"Keep-Alive" ,
    "User-Agent":"okhttp/3.12.1"}
#---------------------------------------------------------------------
data2 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}'
#--------------------------------------------------------------------- 
ctv = requests.post(url2,headers=hd2,data = data2).json()["GenerateTokenResult"]["Token"]
#---------------------------------------------------------------------
a=ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
#---------------------------------------------------------------------
htv=(sha256(a.encode('utf-8')).hexdigest().upper())
#---------------------------------------------------------------------
print(ctv)
#---------------------------------------------------------------------
print(htv)
#---------------------------------------------------------------------
