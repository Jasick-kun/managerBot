import telebot
import pymongo
db=pymongo.MongoClient("mongodb://localhost:27017")
current_db = db["managerBot"]
bot = telebot.TeleBot('5319939801:AAEwAqgrPYhbxM91pl-2BJwcSS5wbaO1bXc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Здравствуйте, как вас зовут?',parse_mode='html')


bot.polling(none_stop=True)