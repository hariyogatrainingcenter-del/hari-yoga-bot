
import os
from flask import Flask, request
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# --- WELCOME MESSAGE ---
@bot.message_handler(commands=['start', 'help'])
def welcome(m):
    text = """🙏 வணக்கம்! Hari Yoga & Battery Academy-க்கு வரவேற்கிறோம்!

🔋 *Batthari Hari AiTech*

⚡ EV Battery Training | Lithium-Ion, LiFePO4, BMS
🧘 Hari Yoga Training Center

👇 Commands:
/yoga - Yoga Training Info
/contact - Contact Details
/battery - Battery Course ₹99

🎥 YouTube: @haribatteryacademy"""

    bot.reply_to(m, text)

@bot.message_handler(commands=['yoga'])
def yoga(m):
    bot.reply_to(m, "🧘 Hari Yoga Training Center - International Yoga Academy\n📞 Contact: /contact")

@bot.message_handler(commands=['contact'])
def contact(m):
    bot.reply_to(m, "📞 90000 00000\n📺 YouTube: https://youtube.com/@haribatteryacademy")

@bot.message_handler(commands=['battery'])
def battery(m):
    bot.reply_to(m, "🔋 Battery Course - ₹99 Only!\nLi-Ion, LiFePO4, BMS Full Training\nEnroll: /contact")

@bot.message_handler(func=lambda m: True)
def all_messages(m):
    bot.reply_to(m, "🙏 வணக்கம் நண்பா! /start என்று Type பண்ணுங்க!")

# --- WEBHOOK ROUTES (இது தான் முக்கியம்) ---
@app.route('/')
def home():
    return "Hari Yoga Bot is LIVE! 🔥"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'ok', 200
    else:
        return 'error', 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
