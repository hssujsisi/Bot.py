from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ReplyKeyboardMarkup, KeyboardButton
import logging

TOKEN = "7915829620:AAGWEi4bSHfc9Ex7EykQxJ2b3zBxewuTjac"
ADMIN_ID = "5040554415"
PORT=5000

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update, context):
    update.message.reply_text(
        "📚 بیاتوانیمه | از سال 1396\n"
        "✉️ ارتباط: bia2anime.com@gmail.com\n\n"
        "برای ثبت نام: /register"
    )

def register(update, context):
    btn = [[KeyboardButton("ارسال شماره 📞", request_contact=True)]]
    update.message.reply_text(
        "لطفاً شماره خود را ارسال کنید:",
        reply_markup=ReplyKeyboardMarkup(btn, resize_keyboard=True)
    )

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('register', register))
from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get('TOKEN')
PORT = int(os.environ.get('PORT', 5000))

def start(update, context):
    update.message.reply_text("ربات فعال است!")

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_webhook(
    listen="0.0.0.0",
    port=PORT,
    url_path=TOKEN,
    webhook_url=f"https://your-app-name.onrender.com/{TOKEN}"
)