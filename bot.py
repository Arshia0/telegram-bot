from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Your bot token
TOKEN = '7211395396:AAGNhfMUDSJdRlOB5DKoH-tjvyWuBotgM60'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام!')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

