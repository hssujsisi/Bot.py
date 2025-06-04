from telegram.ext import Updater, CommandHandler
import os
import logging

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(name)

# خواندن متغیرهای محیطی
TOKEN = os.environ['TOKEN']  # حتماً باید در Render تنظیم شده باشد
PORT = int(os.environ.get('PORT', 5000))
SERVICE_URL = "bot-py-3-eh85.onrender.com"  # نام سرویس شما

def start(update, context):
    update.message.reply_text("✅ ربات فعال شد! /start کار می‌کند")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))

    # تنظیمات webhook برای Render
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://{SERVICE_URL}/{TOKEN}"
    )
    updater.bot.set_webhook(f"https://{SERVICE_URL}/{TOKEN}")
    
    logger.info(f"ربات روی پورت {PORT} شروع به کار کرد")
    updater.idle()

if name == 'main':
    main()