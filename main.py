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
    bot.send_message(message.chat.id, "Здравстуйте, добро пожаловать в нашу компанию, я бот созданный, чтобы помочь вам безболезнено влиться в новый коллектив", reply_markup=markup) # проверить на грамматику и подумать над изменением фразы
    bot.send_message(message.chat.id, "Что вы хотите сделать?\n"
                                      "/start - Активировать бота\n"
                                      "/find - Найти то, что вам нужно\n"
                                      "/complain - Пожаловаться на работу бота или сотрудников", reply_markup=markup)
    bot.send_message(message.chat.id, "Выберите команду", reply_markup=markup)

@bot.message_handler(commands = ['find'])
def find(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Office = types.KeyboardButton("/office")
    Collaborator = types.KeyboardButton("/collaborator")
    Departments = types.KeyboardButton("/departments")
    Another = types.KeyboardButton("/another")
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
    Aeroquantum = types.KeyboardButton("/aeroquantum")
    Promrobokvantum = types.KeyboardButton("/promrobokvantum")
    Industrial_design = types.KeyboardButton("/industrial_design")
    markup.add(IT, VR_AR, Aeroquantum, Promrobokvantum, Industrial_design)
    bot.send_message(message.chat.id, "Какой отдел вам нужен?", reply_markup=markup)

@bot.message_handler(commands=['it'])
def it(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "IT", reply_markup=markup)
    markup.add(types.InlineKeyboardButton("Узнать подробнее", url="https://kvantorium69.ru/it-%d0%ba%d0%b2%d0%b0%d0%bd%d1%82%d1%83%d0%bc/"))  # Текст Кнопки и адрес ссылки

@bot.message_handler(commands=['vr_ar'])
def vr_ar(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "VR/AR", reply_markup=markup)
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/vr-ar/"))  # Текст Кнопки и адрес ссылки

@bot.message_handler(commands=['aeroquantum'])
def aeroquantum(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Аэроквантум", reply_markup=markup)
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d0%b0%d1%8d%d1%80%d0%be%d0%ba%d0%b2%d0%b0%d0%bd%d1%82%d1%83%d0%bc/"))  # Текст Кнопки и адрес ссылки

@bot.message_handler(commands=['promrobokvantum'])
def promrobokvantum(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Промробоквантум", reply_markup=markup)
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d0%bf%d1%80%d0%be%d0%bc%d1%80%d0%be%d0%b1%d0%be%d0%ba%d0%b2%d0%b0%d0%bd%d1%82%d1%83%d0%bc/"))  # Текст Кнопки и адрес ссылки

@bot.message_handler(commands=['industrial_design'])
def id(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Промышленный дизайн", reply_markup=markup)
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d0%bf%d1%80%d0%be%d0%bc%d1%8b%d1%88%d0%bb%d0%b5%d0%bd%d0%bd%d1%8b%d0%b9-%d0%b4%d0%b8%d0%b7%d0%b0%d0%b9%d0%bd/"))  # Текст Кнопки и адрес ссылки

@bot.message_handler(commands=['high_tech'])
def high_tech(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Хайтек", reply_markup=markup)
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/%d1%85%d0%b0%d0%b9-%d1%82%d0%b5%d0%ba/"))  # Текст Кнопки и адрес ссылки

@bot.message_handler(commands=['media'])
def media(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Медиа", reply_markup=markup)
    markup.add(types.InlineKeyboardButton("Узнать подробнее",
                                          url="https://kvantorium69.ru/media/"))  # Текст Кнопки и адрес ссылки

@bot.message_handler(commands = ['complain'])
def complain(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)#Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Collaborator = types.KeyboardButton("/collaborator")
    Bot = types.KeyboardButton("/cot")
    Company_management = types.KeyboardButton("/company_management")
    markup.add(Collaborator, Bot, Company_management)#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "На что вы хотите пожаловаться?", reply_markup=markup)

bot.polling(none_stop=True)