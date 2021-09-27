from re import T
from telegram import Update,update
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters 

from voice import text_to_file

TOKEN="MY_TOKEN"

def hello(update,context) :
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help_handler(update,context):
    help_text="""Используйте этот бот для трансформации текстовых сообщений в голосовые"""
    update.message.reply_text(help_text)

#A little relaxation on the team: "game".

def game_ing(update,context):
    update.message.reply_text("Испытаем удачу?")
    update.message.reply_dice()

#Here, a check for a palindrome is performed; in the case of a palindrome,
#  the text + string is returned; in other cases, the text itself

def reply (update,context):
    text=update.message.text
    if text==text[::-1]:
        mi_file_bay=text_to_file(text+" А Вы знали?,что это-палиндром!")    
    else:
        mi_file_bay=text_to_file(text)
    update.message.reply_voice(voice=open(mi_file_bay,'rb'))

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help',help_handler))
updater.dispatcher.add_handler(CommandHandler('game',game_ing))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~ Filters.command,reply))

updater.start_polling()
updater.idle()