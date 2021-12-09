import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types
bot = telebot.TeleBot("5055186869:AAF0c3BQ42BPcfQsbDzqpYurK_IolxAfdqE", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['start'])
def start(message):
    start_text = 'Hello. You can easily find pictures from google for free on this bot. Made by @shavkatNor'
    bot.send_message(message.chat.id,start_text)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        text = message.text.replace(' ','+')
        sahifa = f"https://www.google.com/search?q={text}&tbm=isch&source=lnms&sa=X"
        r = requests.get(sahifa)
        soup = BeautifulSoup(r.text, 'html.parser')
        get_three = soup.select('img[class="yWs4tf"]')[:10]
        media = []
        for i in get_three:
            media.append(types.InputMediaPhoto(i['src']))
        bot.send_media_group(message.chat.id, media)
    except:
        bot.send_photo(message.chat.id,'Not Found')
bot.infinity_polling()