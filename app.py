import os
from flask import Flask, request
import telebot
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start','help'])
def welcome(m):
    bot.reply_to(m, "🙏 வணக்கம்! Hari Yoga Bot Ready!\n\n/yoga - Yoga Info\n/contact - Contact")

@bot.message_handler(commands=['yoga'])
def yoga(m):
    bot.reply_to(m, "🧘‍♂️ Hari Yoga Training\nDaily Classes Available!")

@bot.message_handler(commands=['contact'])
def contact(m):
    bot.reply_to(m, "📞 90000 00000\n📍 Chennai")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"Neenga: {m.text}")

@app.route('/')
def home():
    return "Bot Live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/setwebhook')
def sethook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url=https://hari-yoga-bot-1.onrender.com/webhook"
    return requests.get(url).text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
