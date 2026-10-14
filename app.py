import os, threading
from flask import Flask
import telebot
TOKEN=os.getenv("BOT_TOKEN")
bot=telebot.TeleBot(TOKEN)
app=Flask(__name__)
@app.route('/')
def home(): return "Batthari Hari Bot OK"
@bot.message_handler(commands=['start','help'])
def welcome(m): bot.reply_to(m, "🙏 வணக்கம்! Hari Yoga & Battery Academy-ku varaverkirom!\n\n🔋 Batthari Hari AiTech\n🧘 Hari Yoga Training\n\nCommands: /yoga /contact /battery\nYouTube: @haribatteryacademy")
@bot.message_handler(commands=['yoga','contact','battery'])
def o(m): bot.reply_to(m, "📞 Contact Hari - YouTube @haribatteryacademy")
def run(): bot.infinity_polling()
threading.Thread(target=run,daemon=True).start()
if __name__=="__main__": app.run(host='0.0.0.0',port=int(os.getenv("PORT",10000)))
