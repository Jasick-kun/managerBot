import telebot
import pymongo
db=pymongo.MongoClient("mongodb://localhost:27017")
current_db = db["managerBot"]
bot = telebot.TeleBot('5319939801:AAEwAqgrPYhbxM91pl-2BJwcSS5wbaO1bXc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Здравствуйте, как вас зовут?',parse_mode='html')
    current_col=current_db["active_user"]
    user = current_col.find_one({"chat_id":message.chat.id})
    if (user.count() == 0):
        newUser = {'first_name': message.from_user.first_name,
                   'second_name': message.from_user.last_name,
                   'chat_id':message.chat.id,
                   'state':0
                   }
        current_col.insert_one(newUser);

@bot.message_handler()
def get_user_text(message):
    current_col = current_db["active_user"]
    user = current_col.find_one({"chat_id":message.chat.id})
    if(user['state']==0):
        login_col = current_db["Login"]
        if(login_col.find_one({'name':message.text}).count()>0):
            questions(message)
        else:bot.send_message(message.chat.id,'Я вас не знаю')
    else:questions(message);


def questions(message):
    active_user_col=current_db["active_user"]
    state=active_user_col.find_one({'chat_id':message.chat.id})['state']
    question_col=current_db["question"]
    q=question_col.find({'is_active':True})

bot.polling(none_stop=True)