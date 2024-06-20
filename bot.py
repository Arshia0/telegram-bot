from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# توکن ربات خود را جایگزین کنید
TOKEN = "7211395396:AAGNhfMUDSJdRlOB5DKoH-tjvyWuBotgM60"
PASSWORD = "122333ashi"

# متغیری برای ذخیره حالت درخواست رمز عبور
user_states = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سلام! این ربات تلگرام شما است.")

def command1(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("عرشیا افشار\nمتولد ۱۳۸۱/۰۱/۲۴\nساکن شهر: همدان / اصفهان\nتحصیلات: کارشناسی برق (گرایش بیوالکتریک)")

def command2(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("gmai: arshiaafshar7@gmail.com\ntelegram: @asshiiv\ninstagram: @asshiiv\nphone-number: 09185842903")

def command3(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_states[user_id] = "waiting_for_password"
    update.message.reply_text("لطفا رمز عبور خود را وارد کنید:")

def handle_password(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_states.get(user_id) == "waiting_for_password":
        if update.message.text == PASSWORD:
            update.message.reply_text("رمز عبور صحیح است. رزومه:\nبه زودی پیوست داده می‌شود")
        else:
            update.message.reply_text("رمز عبور نادرست است. لطفا دوباره تلاش کنید.")
        user_states[user_id] = None

def command4(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("پلی لیست آهنگ:\nپلی لیستی از آهنگ‌ها به زودی اضافه خواهد شد")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("command1", command1))
    dispatcher.add_handler(CommandHandler("command2", command2))
    dispatcher.add_handler(CommandHandler("command3", command3))
    dispatcher.add_handler(CommandHandler("command4", command4))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_password))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
