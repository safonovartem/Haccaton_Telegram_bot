import requests
#from bs4 import BeautifulSoup as b
import telebot
from telebot import types
bot = telebot.TeleBot('6467932346:AAFtWURnHqqU9vHahdDYp5V0x7N_BZL5UIM')

@bot.message_handler(commands=['start']) # Отслеживание команды Старт
def start(message):
    mess = f"Здравствуйте, <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
    if message.from_user.last_name == None:
        mess = f"Привет, <b>{message.from_user.first_name}</b>"
        bot.send_message(message.chat.id, mess, parse_mode="html") #html можно изменить
    elif message.from_user.first_name == None:
        mess = f"Привет,<b>{message.from_user.last_name}</b>"
        bot.send_message(message.chat.id, mess, parse_mode="html")
    else:
        mess = f"Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
        bot.send_message(message.chat.id, mess, parse_mode="html")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)  # Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    start = types.KeyboardButton("/start")
    find = types.KeyboardButton("/find")
    complain = types.KeyboardButton("/complain")
    markup.add(start, find, complain)  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Здравствуйте, добро пожаловать в нашу компанию. Я создан для того, чтобы помочь вам безболезненно влиться в наш дружный коллектив", reply_markup=markup) # проверить на грамматику и подумать над изменением фразы
    bot.send_message(message.chat.id, "Что вы хотите сделать?\n"
                                      "/start - Активировать бота\n"
                                      "/find - Найти то, что вам нужно\n"
                                      "/complain - Пожаловаться на сотрудника или начальника нашей компании", reply_markup=markup)
    bot.send_message(message.chat.id, "Выберите команду", reply_markup=markup)

@bot.message_handler(commands = ['find'])
def find(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Office = types.KeyboardButton("/office")
    Collaborator = types.KeyboardButton("/collaborator")
    Departments = types.KeyboardButton("/departments")
    Another = types.KeyboardButton("/WC")
    markup.add(Office, Collaborator, Departments, Another)  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Что вы хотите найти?", reply_markup=markup)

@bot.message_handler(commands = ['office'])
def office(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посмотреть на карте", url="https://maps.app.goo.gl/QYLcJXSfnLMLdiks9"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Адрес офиса: Студенческий пер., 28, Тверь, Тверская обл., 170100", reply_markup=markup)

@bot.message_handler(commands = ['collaborator'])
def collaborator(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посмотреть список сотрудников", url="https://kvantorium69.ru/%d0%be-%d0%bd%d0%b0%d1%81/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Список сотрудников доступен на сайте",reply_markup=markup)

@bot.message_handler(commands = ['departments'])
def departments(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                       row_width=2)  # Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    IT = types.KeyboardButton("/it")
    VR_AR = types.KeyboardButton("/vr_ar")
    Aeroquantum = types.KeyboardButton("/aero_kvantum")
    Promrobokvantum = types.KeyboardButton("/promrobo_kvantum")
    Industrial_design = types.KeyboardButton("/industrial_design")
    High_tech = types.KeyboardButton("/high_tech")
    Media = types.KeyboardButton("/media")
    Kvantum_chess = types.KeyboardButton("/kvantum_chess")
    Laboratory_bio = types.KeyboardButton("/laboratory_bio")
    Laboratory_auto = types.KeyboardButton("/laboratory_auto")
    Laboratory_energy = types.KeyboardButton("/laboratory_energy")
    Math = types.KeyboardButton("/mathematics")
    English = types.KeyboardButton("/english")
    markup.add(IT, VR_AR, Aeroquantum, Promrobokvantum, Industrial_design, High_tech, Media, Kvantum_chess, Laboratory_bio, Laboratory_auto, Laboratory_energy, Math, English)
    bot.send_message(message.chat.id, "Какой отдел вам нужен?", reply_markup=markup)

@bot.message_handler(commands=['it'])
def it(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее", url="https://kvantorium69.ru/it-%d0%ba%d0%b2%d0%b0%d0%bd%d1%82%d1%83%d0%bc/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "IT находится на первом этаже в коридоре, второй слева кабинет", reply_markup=markup)
@bot.message_handler(commands=['vr_ar'])
def vr_ar(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/vr-ar/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "VR/AR находится на первом этаже в коридоре, четвёртый слева кабинет", reply_markup=markup)
@bot.message_handler(commands=['aero_kvantum'])
def aeroquantum(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d0%b0%d1%8d%d1%80%d0%be%d0%ba%d0%b2%d0%b0%d0%bd%d1%82%d1%83%d0%bc/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Аэроквантум находится на первом этаже в конце коридора справа", reply_markup=markup)
@bot.message_handler(commands=['promrobo_kvantum'])
def promrobokvantum(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d0%bf%d1%80%d0%be%d0%bc%d1%80%d0%be%d0%b1%d0%be%d0%ba%d0%b2%d0%b0%d0%bd%d1%82%d1%83%d0%bc/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Промробоквантум находится на первом этаже в коридоре, первый слева кабинет", reply_markup=markup)
@bot.message_handler(commands=['industrial_design'])
def id(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d0%bf%d1%80%d0%be%d0%bc%d1%8b%d1%88%d0%bb%d0%b5%d0%bd%d0%bd%d1%8b%d0%b9-%d0%b4%d0%b8%d0%b7%d0%b0%d0%b9%d0%bd/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Промышленный дизайн находится на первом этаже в коридоре, пятый слева кабинет", reply_markup=markup)

@bot.message_handler(commands=['high_tech'])
def high_tech(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d1%85%d0%b0%d0%b9-%d1%82%d0%b5%d0%ba/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Хайтек находится на первом этаже в коридоре, первый справа кабинет", reply_markup=markup)

@bot.message_handler(commands=['media'])
def media(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/media/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Обычно занятия у Медиа проходят в конферен зале, но лучше уточнить на ресепшне", reply_markup=markup)

@bot.message_handler(commands=['kvantum_chess'])
def kvantum_chess(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d1%88%d0%b0%d1%85%d0%bc%d0%b0%d1%82%d1%8b/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Шахматы находится на первом этаже в коридоре, третий справа кабинет", reply_markup=markup)

@bot.message_handler(commands=['laboratory_bio'])
def laboratory_bio(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/bio-lab/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Лаборатория Био находится на третьем этаже в коридоре, первый слева кабинет", reply_markup=markup)

@bot.message_handler(commands=['laboratory_auto'])
def laboratory_auto(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/auto-lab/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Лаборатория Авто находится на третьем этаже в коридоре, первый справа кабинет", reply_markup=markup)

@bot.message_handler(commands=['laboratory_energy'])
def laboratory_energy(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/energy-lab/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Лаборатория Энерджи находится на третьем этаже в коридоре, третий справа кабинет", reply_markup=markup)

@bot.message_handler(commands=['mathematics'])
def mathematics(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d0%bc%d0%b0%d1%82%d0%b5%d0%bc%d0%b0%d1%82%d0%b8%d0%ba%d0%b0/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Математика находится на первом этаже в коридоре, третий справа кабинет", reply_markup=markup)

@bot.message_handler(commands=['english'])
def english(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d0%b0%d0%bd%d0%b3%d0%bb%d0%b8%d0%b9%d1%81%d0%ba%d0%b8%d0%b9-%d1%8f%d0%b7%d1%8b%d0%ba/"))  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Английский находится на первом этаже в коридоре, третий справа кабинет", reply_markup=markup)


@bot.message_handler(commands = ['WC'])
def another(message):
    bot.send_message(message.chat.id, "Туалеты находятся на 1, 2 и 3 этаже рядом со входом на этот этаж ", parse_mode='html')

@bot.message_handler(commands = ['complain'])
def complain(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)#Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Colleagues = types.KeyboardButton("/сolleagues")
    Company_management = types.KeyboardButton("/company_management")
    markup.add(Colleagues, Company_management)#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "На кого вы хотите пожаловаться?", reply_markup=markup)

@bot.message_handler(commands = ['сolleagues'])
def сolleagues(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)#Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Bulling = types.KeyboardButton("/bulling")
    Harassment = types.KeyboardButton("/harassment")
    Another = types.KeyboardButton("/another")
    markup.add(Bulling, Harassment, Another)#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Укажите причину", reply_markup=markup)

@bot.message_handler(commands = ['bulling'])
def bulling(message):
    bot.send_message(message.chat.id, "Спасибо что сообщили нам об этом, мы немедленно примем меры. Также советуем обратиться в полицию по телефону доверия 8 (4822) 32-95-52.", parse_mode='html')

@bot.message_handler(commands = ['harassment'])
def harassment(message):
    bot.send_message(message.chat.id, "Спасибо что сообщили нам об этом, мы немедленно примем меры. Также советуем обратиться в полицию по телефону доверия 8 (4822) 32-95-52.", parse_mode='html')

@bot.message_handler(commands = ['another'])
def another(message):
    bot.send_message(message.chat.id, "Вы можете написать нам на почту: info@kvantorium69.ru или позвонить по телефону 84822416103, а также советуем обратиться в полицию по телефону доверия 8 (4822) 32-95-52.", parse_mode='html')

@bot.message_handler(commands = ['company_management'])
def сolleagues(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)#Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Bulling = types.KeyboardButton("/bulling")
    Harassment = types.KeyboardButton("/harassment")
    Another = types.KeyboardButton("/another")
    markup.add(Bulling, Harassment, Another)#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Укажите причину", reply_markup=markup)

bot.polling(none_stop=True)