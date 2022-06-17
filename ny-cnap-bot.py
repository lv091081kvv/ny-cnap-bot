# chatbot for cnap of Novoiavorivsk city
import telebot

bot = telebot.TeleBot('5524104596:AAGYVLYuPzAlBICN40434FPsuxbsNXbqq8g')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Добрий день <b>{message.from_user.first_name} {message.from_user.last_name}</b>\nВас вітає ЦНАП Новояворівської міської ради."
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if message.text == "id":
        mess = f"Your ID= {message.from_user.id}"
    elif message.text == "photo":
        photo = open('smile.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, "FILEID")
    else:
        mess = "Вибачте. Я вас не розумію."
        
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)