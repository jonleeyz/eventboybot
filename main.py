import logging
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from secrets import BOT_TOKEN


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Hi there, I am EventBoy, your errand boy for your events!\n\n"
                         + "Choose /help if you are unsure how to proceed!")


def help(bot, update, args):
    help_text = "/start\n/help\n/baba\n/ali"
    if args:
        help_text = help_text[:18]
    
    bot.send_message(chat_id=update.message.chat_id,
                     text=help_text)


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=update.message.text)



updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help, pass_args=True)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
