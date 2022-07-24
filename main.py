import telebot
import requests
import os
import random
import time
token = "5545279600:AAG536spuk4bFBaeLUT96WlpPo9BMHyz5y0"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hi {message.from_user.first_name},\n=== === ===\nWellcome! Send Number & Password To Activate \n Exmple = number:password </strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def ps(message):
    msg = message.text
    number = msg.split(':')[0]
    password = msg.split(':')[1]
    bot.send_message(message.chat.id,f"<strong>Done Recived.. Wait! </strong>",parse_mode="html")
    message =number+":"+password
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    d="Basic"+" "+base64_message
    url='https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan'
    hd={"applicationVersion": "2",
              "applicationName": "MAB",
              "Accept": "text/xml",
              "applicationPassword": "ZFZyqUpqeO9TMhXg4R/9qs0Igwg\u003d",
              "Authorization":d,
              "APP-BuildNumber": "547",
              "APP-Version": "22.13.0",
              "OS-Type": "Android",
              "OS-Version": "8",
              "APP-STORE": "Huawei",
              "Is-Corporate": "false",
              "Content-Type": "text/xml; charset\u003dUTF-8",
              "Content-Length": "290",
              "Host": "mab.etisalat.com.eg:11003",
              "Connection": "Keep-Alive",
              "Accept-Encoding": "gzip",
              "User-Agent": "okhttp/3.12.8",
              "ADRUM_1": "isMobile:true",
              "ADRUM": "isAjax:true"}
    data="<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType>J19SG</modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
    r=requests.post(url, headers=hd, data=data)
    coki = r.headers["Set-Cookie"]
    token = coki[:-127]
    bot.send_message(message.chat.id,f"<strong>Done Login : {token}</strong>",parse_mode="html")
bot.polling()
