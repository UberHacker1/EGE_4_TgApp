from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Команда для запуска мини-приложения
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Открыть мини-приложение", web_app={"url": "https://ваш-хостинг.ру"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Нажмите кнопку, чтобы начать:", reply_markup=reply_markup)

# Основная функция
def main():
    updater = Updater("7202820544:AAEd0KJbxzsOpH_sAUEXVywWU0Tho7KxsaQ")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()