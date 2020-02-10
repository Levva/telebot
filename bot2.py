import telebot

bot = telebot.TeleBot('1045427310:AAHFS0cyYtvPvsNh3VkX2FbTVZp5g9o57Gw')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Ты написал мне /start!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, моя проматерь')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, проматерь')
    elif message.text.lower() == 'я люблю тебя':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANYXj_wBLDW_GHj7zR_aCHiJFRSFFwAAsQEAAJH-wkMukx_9SwpPxoYBA')


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока', 'Я люблю тебя')

bot.polling()
