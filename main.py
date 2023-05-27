
import os
from bs4 import BeautifulSoup
import requests
import telebot
import schedule
import time
from telegram import *

allinfoc = '@eyetayeknew2'
maininfoc = '@eyetayeknew'
API_KEY = '5725056481:AAE0Nw1HvojWL-yBxyvOBkIZbWT1R9lYlPA'
bot = telebot.TeleBot(API_KEY)

url = requests.get('https://www.skysports.com/premier-league-table')
soup = BeautifulSoup(url.content, 'html.parser')
table = soup.find('table')
body = soup.find('tbody')
tr = body.find_all('tr')
r = ''
for t in tr:
    td = t.find_all('td')
    
    rt = td[0]
    rtt = td[1]
    rttt = td[2]
    rtttt = td[8]
    rttttt = td[9]
    p =  rt.text +', ' + rtt.text.replace("\n", "") + '\n'+ '#Played : ' + rttt.text + ' || #Goals : ' + rtttt.text + ' || #Points : ' + rttttt.text
    r += p + '\n'
@bot.message_handler(commands=['table', 'start'])
def boxo(message):

 bot.send_message(message.chat.id,'\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\n' +r +'\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\U000026bd\n')
 bot.send_message(message.chat.id,'\U000026bd\U000026bd\U000026bd\U000026bd  \n\U000026bd/table\U000026bd  \n\U000026bd\U000026bd\U000026bd\U000026bd')
 allinfo = str(message) + "\n Using  @epl_table_bot"
 maininfo = ' #Username  @' + str(message.from_user.username) + '\n #FirstName  ' + str(message.from_user.first_name) +'\n #LastName  ' + str(message.from_user.last_name) + '\n #ID  ' + str(message.from_user.id) 
 bot.send_message(maininfoc, maininfo + "\n Using @epl_table_bot")
 bot.send_message(allinfoc,allinfo )  

@bot.message_handler(commands=['about', 'About', 'ABOUT'])
def about(message):
 bot.send_message(message.chat.id,' | @eyob2m')

bot.polling() 
