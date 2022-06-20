# chatbot for cnap of Novoiavorivsk city
import telebot
from telebot import types

bot = telebot.TeleBot('5524104596:AAGYVLYuPzAlBICN40434FPsuxbsNXbqq8g')

# send user command start
@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Добрий день <b>{message.from_user.first_name} {message.from_user.last_name}</b>\nВас вітає ЦНАП Новояворівської міської ради."
    bot.send_message(message.chat.id, mess, parse_mode='html')

# send user command finish
@bot.message_handler(commands=['finish'])
def start(message):
    mess = f"Дякую <b>{message.from_user.first_name} {message.from_user.last_name}</b> що нас відвідали.\nГарного дня."
    bot.send_message(message.chat.id, mess, parse_mode='html')

# send user text
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "id":
#         mess = f"Your ID= {message.from_user.id}"
#     elif message.text == "photo":
#         photo = open('smile.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#         bot.send_photo(message.chat.id, "FILEID")
    # else:
    #     mess = "Вибачте. Я вас не розумію."
    #
    # bot.send_message(message.chat.id, mess, parse_mode='html')

# send user photo
@bot.message_handler(content_types=['photo'])
def get_user_text(message):
    bot.send_message(message.chat.id, 'Гарне фото', parse_mode='html')

# create link to site
@bot.message_handler(commands=['website'])
def get_user_text(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url="https://novoyavmiskrada.org.ua"))
    bot.send_message(message.chat.id, '&#8595 Натисніть на ссилку для переходу на офіційний сайт &#8595'
                     , parse_mode='html', reply_markup=markup)


# create buttons
@bot.message_handler(commands=['help'])
def get_user_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('/start')
    finish = types.KeyboardButton('/finish')
    markup.add(start, finish, website)
    bot.send_message(message.chat.id, 'Виберіть необхідний варіант'
                     , parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)