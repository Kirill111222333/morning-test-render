from flask import Flask
import telebot
import os

app = Flask(__name__)
bot = telebot.TeleBot(os.environ['TELEGRAM_API_TOKEN'])
CHAT_ID = os.environ['MY_CHAT_ID']

@app.route('/')
def hello():
    return "Bot is running!"

if __name__ == '__main__':
    bot.send_message(CHAT_ID, "доброго ранку!")
    app.run(host='0.0.0.0', port=10000)
