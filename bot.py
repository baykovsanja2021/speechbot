# Импортируем необходимую документацию для работы с кодом нашего Telegram бота.
from telegram import Update,update
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters 
# Импорт библиотеки модулей преобразования текстовых сообщений в голосовые 
from voice import text_to_file

# Подставляем вместо "MY_TOKEN" значение своего TOKEN,полученого на BotFather.
TOKEN="MY_TOKEN"

# Функция,которая выводит приветственное сообщение,при введении команды "/hello"
# обращаясь по имени к пользователю.
def hello(update,context) :
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Определяем обработчик команды "/help".
# Функция,возвращает вспомогательный текст отображающий применение этого бота
def help_handler(update,context):
# переменная help_text назначена для "гигиены" кода.
    help_text="""Используйте этот бот для трансформации текстовых сообщений в голосовые"""
    update.message.reply_text(help_text)

# Даная функция определяет обработчик команды"/game".
def game_ing(update,context):
# При вводе команды выводит текст "Испытаем удачу?"   
    update.message.reply_text("Испытаем удачу?")
    # и анимацию игровой кости для небольшого релакса.
    update.message.reply_dice()

# В этой функции делаем проверку текста на палиндром,если слово-палиндром,то
# возвращается (text+строка: А Вы знали...),в остальных случаях только (text).
# В строке,знаки препинания проставлены не по синктаксису для более корректного 
# озвучивания голосовым движком текста.
def reply (update,context):
    text=update.message.text
    if text==text[::-1]:
        sounds_sign=text_to_file(text+" А Вы знали?,что это-палиндром!")    
    else:
        sounds_sign=text_to_file(text)
# Вызываем голосовое сообщение из текста пользователя.        
    update.message.reply_voice(voice=open(sounds_sign,'rb'))

# Передаем созданому здесь Updater,TOKEN вашего бота.   
updater = Updater(TOKEN)

# Получить диспетчер для регистрации обработчиков,
#  по разным командам - ​​ответ в Telegram.
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help',help_handler))
updater.dispatcher.add_handler(CommandHandler('game',game_ing))
# при отсутствии команды, т.е. сообщении - повторить сообщение в Telegram.
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~ Filters.command,reply))

 # Запускаем бота.
updater.start_polling()
# Запускать бота, пока вы не нажмете Ctrl-C
# Это следует использовать в большинстве случаев, так как
# start_polling () не блокирует и корректно останавливает бота. 
updater.idle()