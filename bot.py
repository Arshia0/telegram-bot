from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext

# توکن ربات
TOKEN = '7211395396:AAGNhfMUDSJdRlOB5DKoH-tjvyWuBotgM60'

# تابع برای شروع ربات
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("مشخصات", callback_data='1'),
            InlineKeyboardButton("رزومه کاری", callback_data='2'),
            InlineKeyboardButton("آی‌دی شبکه‌های اجتماعی", callback_data='3')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('یکی از گزینه‌ها را انتخاب کنید:', reply_markup=reply_markup)

# تابع برای مدیریت فشردن دکمه‌ها
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == '1':
        await query.edit_message_text(text="لطفاً مشخصات خود را به این صورت وارد کنید: اسم، فامیل، شماره تلفن، ایمیل")
    elif query.data == '2':
        await query.edit_message_text(text="در حال ارسال فایل رزومه کاری...")
        # ارسال فایل PDF (اطمینان حاصل کنید که مسیر فایل صحیح است)
        await context.bot.send_document(chat_id=query.message.chat_id, document=open('resume.pdf', 'rb'))
    elif query.data == '3':
        await query.edit_message_text(text="لطفاً آی‌دی‌های شبکه‌های اجتماعی خود را به این صورت وارد کنید: تلگرام، واتس‌اپ، اینستاگرام")

# تابع برای مدیریت پیام‌های متنی
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    await update.message.reply_text(f'شما وارد کردید: {text}')

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
