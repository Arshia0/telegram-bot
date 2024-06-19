from telegram import Update, Bot, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7211395396:AAGNhfMUDSJdRlOB5DKoH-tjvyWuBotgM60'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "سلام! به بات من خوش آمدید. "
        "از دستورات زیر می‌توانید استفاده کنید:\n"
        "/info - مشخصات فردی\n"
        "/contact - لینک های ارتباطی\n"
        "/resume - رزومه"
    )

def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "مشخصات فردی:\n"
        "عرشیا افشار\n"
        "متولد ۱۳۸۱/۰۱/۲۴\n"
        "ساکن شهر: همدان / اصفهان\n"
        "تحصیلات: کارشناسی برق (گرایش بیوالکتریک)"
    )

def contact(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "لینک های ارتباطی:\n"
        "Gmail: arshiaafshar7@gmail.com\n"
        "Telegram: @asshiiv\n"
        "Instagram: @asshiiv\n"
        "Phone Number: 09185842903"
    )

def resume(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "رزومه:\n"
        "به زودی پیوست داده میشود"
    )

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("contact", contact))
    dispatcher.add_handler(CommandHandler("resume", resume))

    updater.start_webhook(listen="0.0.0.0",
                          port=8443,
                          url_path=TOKEN,
                          webhook_url=f"https://your-domain.com/{TOKEN}")
    updater.idle()

if __name__ == '__main__':
    main()
