from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
import json

# Пример данных заданий
tasks = [
    {
        "question": "Укажите варианты ответов, в которых верно выделена буква, обозначающая ударный гласный звук. Запишите номера ответов.",
        "options": [
            "1)  созЫв",
            "2)  Отзыв (посла из страны)",
            "3)  дОнизу",
            "4)  оптОвый",
            "5)  аэропортЫ"
        ],
        "correctAnswers": [2, 5]
    },
    {
        "question": "Укажите варианты ответов, в которых верно выделена буква, обозначающая ударный гласный звук. Запишите номера ответов.",
        "options": [
            "1)  звонИт",
            "2)  красИвее",
            "3)  кУхонный",
            "4)  тОрты",
            "5)  средствА"
        ],
        "correctAnswers": [1, 2, 5]
    }
]

# Команда для запуска мини-приложения
async def start(update: Update, context: CallbackContext):
    # Преобразуем данные заданий в JSON
    tasks_json = json.dumps(tasks)
    
    # Создаем кнопку для открытия мини-приложения
    keyboard = [
        [InlineKeyboardButton("Открыть мини-приложение", web_app={"url": "https://ege4tgapp.vercel.app"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        "Нажмите кнопку, чтобы начать:",
        reply_markup=reply_markup
    )

# Основная функция
def main():
    # Вставьте сюда ваш токен
    application = Application.builder().token("7202820544:AAEd0KJbxzsOpH_sAUEXVywWU0Tho7KxsaQ").build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()