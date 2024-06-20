from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# توکن ربات خود را جایگزین کنید
TOKEN = "7211395396:AAGNhfMUDSJdRlOB5DKoH-tjvyWuBotgM60"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سلام! این ربات تلگرام شما است.")

def command1(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("عرشیا افشار\nمتولد ۱۳۸۱/۰۱/۲۴\nساکن شهر: همدان / اصفهان\nتحصیلات: کارشناسی برق (گرایش بیوالکتریک)")

def command2(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("gmai: arshiaafshar7@gmail.com\ntelegram: @asshiiv\ninstagram: @asshiiv\nphone-number: 09185842903")

def command3(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("رزومه:\nبه زودی پیوست داده می‌شود")

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

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
