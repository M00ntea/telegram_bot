import telebot
import wikipedia

wikipedia.set_lang('ru')

TOKEN = '6786921909:AAEAR7sRlxIU-xXNUDe5J_FkAE78cDHZ0GU'

bot = telebot.TeleBot(TOKEN)

dialog_started = False


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Как я могу вам помочь?')


@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, 'вот мой список команд /start /help')


@bot.message_handler(content_types=['text'])
def talk(message):
    global dialog_started

    if not dialog_started:
        if message.text.lower() in ('привет', 'здравствуйте', 'добрый день', 'добрый вечер'):
            user_name = message.from_user.first_name
            response = f"Здравствуйте, {user_name}, чем я могу помочь?"
            bot.send_message(message.chat.id, response)
            dialog_started = True
        else:
            message_user = message.text
            message_user = message_user.replace(' ', '_')
            page = wikipedia.page(message_user)
            bot.send_message(message.chat.id, page.summary)



bot.polling(none_stop=True)
