from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# توکن ربات خود را جایگزین کنید
TOKEN = "7211395396:AAGNhfMUDSJdRlOB5DKoH-tjvyWuBotgM60"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("سلام! این ربات تلگرام شما است.")

async def command1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("عرشیا افشار\nمتولد ۱۳۸۱/۰۱/۲۴\nساکن شهر: همدان / اصفهان\nتحصیلات: کارشناسی برق (گرایش بیوالکتریک)")

async def command2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("gmai: arshiaafshar7@gmail.com\ntelegram: @asshiiv\ninstagram: @asshiiv\nphone-number: 09185842903")

async def command3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("رزومه:\nبه زودی پیوست داده می‌شود")

async def command4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("پلی لیست آهنگ:\nپلی لیستی از آهنگ‌ها به زودی اضافه خواهد شد")

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("command1", command1))
    application.add_handler(CommandHandler("command2", command2))
    application.add_handler(CommandHandler("command3", command3))
    application.add_handler(CommandHandler("command4", command4))

    application.run_polling()

if __name__ == "__main__":
    main()
