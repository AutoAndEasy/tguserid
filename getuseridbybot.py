from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello World!')

def echo(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    update.message.reply_text(f"Your message: {update.message.text}\nYour ID: {user_id}")

def main() -> None:
    updater = Updater("TOKEN", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
