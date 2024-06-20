from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# توکن ربات خود را جایگزین کنید
TOKEN = "7211395396:AAGNhfMUDSJdRlOB5DKoH-tjvyWuBotgM60"
PASSWORD = "122333ashi"

# متغیری برای ذخیره حالت درخواست رمز عبور
user_states = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("سلام! این ربات تلگرام شما است.")

async def command1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("عرشیا افشار\nمتولد ۱۳۸۱/۰۱/۲۴\nساکن شهر: همدان / اصفهان\nتحصیلات: کارشناسی برق (گرایش بیوالکتریک)")

async def command2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("gmai: arshiaafshar7@gmail.com\ntelegram: @asshiiv\ninstagram: @asshiiv\nphone-number: 09185842903")

async def command3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    user_states[user_id] = "waiting_for_password"
    await update.message.reply_text("لطفا رمز عبور خود را وارد کنید:")

async def handle_password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    if user_states.get(user_id) == "waiting_for_password":
        if update.message.text == PASSWORD:
            await update.message.reply_text("رمز عبور صحیح است. در حال ارسال رزومه...")
            try:
                await update.message.reply_document(open('resume.pdf', 'rb'))
            except Exception as e:
                await update.message.reply_text(f"خطا در ارسال رزومه: {e}")
        else:
            await update.message.reply_text("رمز عبور نادرست است. لطفا دوباره تلاش کنید.")
        user_states[user_id] = None

async def command4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("پلی لیست آهنگ:\nپلی لیستی از آهنگ‌ها به زودی اضافه خواهد شد")

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("command1", command1))
    application.add_handler(CommandHandler("command2", command2))
    application.add_handler(CommandHandler("command3", command3))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_password))

    application.run_polling()

if __name__ == '__main__':
    main()
