from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters




TG_TOKEN = '1045427310:AAHFS0cyYtvPvsNh3VkX2FbTVZp5g9o57Gw'


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    print(user)
    if user:
        name = user.first_name
    else:
        name = 'anonimuse'
    print(name)
    text = update.effective_message.text
    print(text)
    reply_text = f'Hello, {name}!\n\n{text}'

    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )


def main():
    print('Start')
    bot = Bot(
        token=TG_TOKEN,
        # base_url='socks5h://61.41.9.213:10081',
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )
    print('Start1')

    handler = MessageHandler(Filters.all, message_handler)
    print(handler)

    updater.dispatcher.add_handler(handler)
    print('Start4')

    updater.start_polling()
    print('Start5')

    updater.idle()
    print('Start6')

    print('Finish')

if __name__ == '__main__':
    main()

