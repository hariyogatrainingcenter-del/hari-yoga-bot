import os, threading
from flask import Flask
import telebot

TOKEN=os.getenv("BOT_TOKEN")
PRIVATE_CHANNEL_ID=-1004428761233
bot=telebot.TeleBot(TOKEN)
app=Flask(__name__)

@app.route('/')
def home(): return "Batthari Hari Bot OK - Voice Added!"

@bot.message_handler(commands=['start','help'])
def welcome(m):
    bot.reply_to(m, "🙏 வணக்கம்! Batthari Hari Yoga Training Center-க்கு வரவேற்கிறோம்!")
    try: bot.send_message(PRIVATE_CHANNEL_ID, f"New User: {m.from_user.first_name} - {m.from_user.id}")
    except: pass

@bot.message_handler(commands=['yoga','contact','course'])
def o(m):
    bot.reply_to(m, "📞 Contact Hari Batthari: 98942 97262 - EV Battery & Yoga Training!")
    try: bot.send_message(PRIVATE_CHANNEL_ID, f"Contact asked by: {m.from_user.first_name}")
    except: pass

# --- VOICE FEATURE ---
@bot.message_handler(content_types=['voice','audio'])
def voice_reply(m):
    bot.reply_to(m, "🎤 Voice message received Swami! We will contact you soon!")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    try: bot.send_message(PRIVATE_CHANNEL_ID, f"Msg from {m.from_user.first_name}: {m.text}")
    except: pass

def run(): bot.infinity_polling()
threading.Thread(target=run,daemon=True).start()
if __name__=="__main__": app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
