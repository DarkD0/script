import telebot
import requests
import os
import random
import time
token = "5400141055:AAGwQDwGR9ojA0qgie_ruTJ9nE2Ghfkole8"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hi {message.from_user.first_name},\n=== === ===\nWellcome! Send Dark To Active </strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def ps(message):
    msg = message.text
    if msg == "Dark":
        bot.send_message(message.chat.id,f"<strong>Done Recived.. Wait! </strong>",parse_mode="html")
        n = '0123456789'
        l = 'abcdefghijklmnopqrstuvwxyz'
        nam = ['ahmed','mohamed','wael','essam','moka','ismail','mahmoud','anas','salah']
        name = random.choice(nam)
        number = '01'+random.choice('0125')+random.choice(n)+random.choice(n)+random.choice(n)+random.choice(n)+random.choice(n)+random.choice(n)+random.choice(n)+random.choice(n)
        email = random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l)
#         print(number)
#         print(email)
        url = "https://api.rida-egypt.xyz/api/user/register"
        hd = {"Host":"api.rida-egypt.xyz"}
        data = {"phone":number,"password":number,"email":email+"@gmail.com","full_name":name}
        r = requests.post(url,headers=hd,data=data).json()
        bot.send_message(message.chat.id,f"<strong> Done Create Account : {number} \nPassword : {number}</strong>",parse_mode="html")
bot.polling()
