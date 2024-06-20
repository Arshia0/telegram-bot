from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# توکن ربات و رمز عبور
TOKEN = "7211395396:AAGNhfMUDSJdRlOB5DKoH-tjvyWuBotgM60"
PASSWORD = "122333ashi"

# متغیری برای ذخیره حالت درخواست رمز عبور
user_states = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! خوش آمدید. از دستور /command1، /command2، /command3، یا /command4 استفاده کنید.")

def personal_info(update: Update, context: CallbackContext):
    update.message.reply_text("عرشیا افشار\nمتولد ۱۳۸۱/۰۱/۲۴\nساکن شهر: همدان / اصفهان\nتحصیلات: کارشناسی برق (گرایش بیوالکتریک)")

def contact_links(update: Update, context: CallbackContext):
    update.message.reply_text("ایمیل: arshiaafshar7@gmail.com\nتلگرام: @asshiiv\nاینستاگرام: @asshiiv\nشماره تماس: 09185842903")

def resume(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    user_states[chat_id] = "awaiting_password"
    update.message.reply_text("لطفاً رمز عبور را وارد کنید:")

def password_check(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if user_states.get(chat_id) == "awaiting_password":
        if update.message.text == PASSWORD:
            update.message.reply_document(document=open("resume.pdf", "rb"))
            update.message.reply_text("رزومه ارسال شد.")
        else:
            update.message.reply_text("رمز عبور اشتباه است.")
        user_states.pop(chat_id, None)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("دستور ناشناخته است.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("command1", personal_info))
    dp.add_handler(CommandHandler("command2", contact_links))
    dp.add_handler(CommandHandler("command3", resume))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, password_check))

    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
