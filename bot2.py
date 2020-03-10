import telebot
import config

bot = telebot.TeleBot(config.token)
print('telebot ok')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я напишу за тебя письмо в ЦИП.', reply_markup=keyboard1)

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     bot.send_message(message.chat.id, 'Мне нужно знать твои ФИО')
#     fio = message.text
#     bot.send_message(message.chat.id, 'Мне нужно знать твой ЦИПовский мейл. Можешь ввести только до @c-i-p.ru')
#     user_email = message.text

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай')
    elif message.text.lower() == 'чирик':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANYXj_wBLDW_GHj7zR_aCHiJFRSFFwAAsQEAAJH-wkMukx_9SwpPxoYBA')

# @bot.message_handler(content_types=['sticker'])
# def send_sticker(message):
#     print(message)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('привет', 'пока', 'чирик')

bot.polling()
