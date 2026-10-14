import os, threading
from flask import Flask
import telebot
TOKEN=os.getenv("BOT_TOKEN")
PRIVATE_CHANNEL_ID=-1004428761233
bot=telebot.TeleBot(TOKEN)
app=Flask(__name__)
@app.route('/')
def home(): return "Batthari Hari Bot OK - Private Active"
@bot.message_handler(commands=['start','help'])
def welcome(m):
    bot.reply_to(m, "🙏 வணக்கம்! Batthari Hari Bot")
    try: bot.send_message(PRIVATE_CHANNEL_ID, f"New User: {m.from_user.first_name} ID:{m.from_user.id}")
    except: pass
@bot.message_handler(commands=['yoga','contact','battery'])
def o(m):
    bot.reply_to(m, "📞 Contact Hari Battery Academy")
    try: bot.send_message(PRIVATE_CHANNEL_ID, f"User {m.from_user.first_name}: {m.text}")
    except: pass
def run(): bot.infinity_polling()
threading.Thread(target=run,daemon=True).start()
if __name__=="__main__": app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
