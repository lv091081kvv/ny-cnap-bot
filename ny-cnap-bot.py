# chatbot for cnap of Novoiavorivsk city
import telebot

bot = telebot.TeleBot('5524104596:AAGYVLYuPzAlBICN40434FPsuxbsNXbqq8g')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Вас вітає ЦНАП м.Новояворівськ", parse_mode='html')



bot.polling(none_stop=True)