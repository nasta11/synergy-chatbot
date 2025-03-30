from telegram.ext import Updater, MessageHandler, Filters

def simple_bot(message):
    message = message.lower()

    responses = {
        "привет": "Привет! Чем могу помочь?",
        "факультеты": "У нас есть 17 факультетов: бизнеса, IT, психологии и др. Подробнее на сайте.",
        "поступление": "Ознакомиться с правилами поступления можно на сайте: https://synergy.ru",
        "расписание": "Расписание занятий доступно в личном кабинете студента.",
        "контакты": "Телефон приёмной комиссии: +7 (495) 225-30-05",
        "до свидания": "До свидания! Удачи в обучении.",
        "пока": "Всего доброго! Обращайтесь ещё."
    }

    for key in responses:
        if key in message:
            return responses[key]
    return "Извините, я не совсем понял. Попробуйте переформулировать вопрос."

def handle_message(update, context):
    user_message = update.message.text
    response = simple_bot(user_message)
    update.message.reply_text(response)

def main():
    updater = Updater("7714330972:AAFL_UzWWd2GDEPhAuP-7Yz_6ZYG45hhiFU", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("🤖 Telegram-бот запущен. Открой Telegram и напиши ему!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
