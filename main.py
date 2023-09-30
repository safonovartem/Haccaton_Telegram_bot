import requests
from bs4 import BeautifulSoup as b
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
                                      "/complain - Пожаловаться на работу бота или сотрудников нашей компании", reply_markup=markup)
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
    URL = "https://www.afisha.ru/tver/events/movies/"

@bot.message_handler(commands = ['complain'])
def complain(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)#Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Collaborator = types.KeyboardButton("/Collaborator")
    Bot = types.KeyboardButton("/Bot")
    Company_management = types.KeyboardButton("/Сompany_management")
    markup.add(Collaborator, Bot, Company_management)#Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "На что вы хотите пожаловаться?", reply_markup=markup)

@bot.message_handler(commands= ['Films_in_Tver'])
def films_in_tver(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши", url="https://www.afisha.ru/tver/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/tver/events/movies/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_films_Tver = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_films_Tver]

    Text_films_Tver = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще',
                   '«Афиша» в соц. сетях',
                   'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время',
                   'Рассылка «Афиши»: главные события недели — у вас на почте']
    def remove_common(Text_films_Tver, Trach_words):
        for i in Text_films_Tver[:]:
            if i in Trach_words:
                Text_films_Tver.remove(i)
                Trach_words.remove(i)

    c = remove_common(Text_films_Tver, Trach_words)

    for i in Text_films_Tver:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это фильмы, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть трейлер прямо на сайте Афиши",reply_markup=markup)  # Возможно эту строку надо перенести в конец

@bot.message_handler(commands= ['Сoncerts_in_Tver'])
def films_in_tver(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши", url="https://www.afisha.ru/tver/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/tver/events/concerts/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_for_films = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_for_films]

    Text_concerts_Tver = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще',
                   '«Афиша» в соц. сетях',
                   'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время',
                   'Рассылка «Афиши»: главные события недели — у вас на почте']

    def remove_common(Text_concerts_Tver, Trach_words):
        for i in Text_concerts_Tver[:]:
            if i in Trach_words:
                Text_concerts_Tver.remove(i)
                Trach_words.remove(i)

    c = remove_common(Text_concerts_Tver, Trach_words)

    for i in Text_concerts_Tver:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это концерты, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть описание прямо на сайте Афиши", reply_markup=markup)  # Возможно эту строку надо перенести в конец

@bot.message_handler(commands = ['Moscow'])
def Msc_city(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)  # Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Movie = types.KeyboardButton("/Films_in_Moscow")
    Concerts = types.KeyboardButton("/Сoncerts_in_Moscow")
    markup.add(Movie, Concerts)  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Отлично, теперь выберите какой тип мероприятий вас интересует", reply_markup=markup)

@bot.message_handler(commands= ['Films_in_Moscow'])
def films_Msc(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши", url="https://www.afisha.ru/msk/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/msc/events/movies/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_films_Msc = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_films_Msc]

    Text_films_Msc = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще',
                   '«Афиша» в соц. сетях',
                   'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время',
                   'Рассылка «Афиши»: главные события недели — у вас на почте']

    def remove_common(Text_films_Msc, Trach_words):
        for i in Text_films_Msc[:]:
            if i in Trach_words:
                Text_films_Msc.remove(i)
                Trach_words.remove(i)

    c = remove_common(Text_films_Msc, Trach_words)

    for i in Text_films_Msc:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это фильмы, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть трейлер прямо на сайте Афиши",reply_markup=markup)  # Возможно эту строку надо перенести в конец
@bot.message_handler(commands= ['Сoncerts_in_Moscow'])
def concerts_Msc(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши", url="https://www.afisha.ru/msk/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/msk/events/concerts/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_concerts_Msc = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_concerts_Msc]

    Text_concerts_Msc = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще',
                   '«Афиша» в соц. сетях',
                   'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время',
                   'Рассылка «Афиши»: главные события недели — у вас на почте']

    def remove_common(Text_concerts_Msc, Trach_words):
        for i in Text_concerts_Msc[:]:
            if i in Trach_words:
                Text_concerts_Msc.remove(i)
                Trach_words.remove(i)

    c = remove_common(Text_concerts_Msc, Trach_words)

    for i in Text_concerts_Msc:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это концерты, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть описание прямо на сайте Афиши", reply_markup=markup)  # Возможно эту строку надо перенести в конец

@bot.message_handler(commands = ['Saint_Petersburg'])
def tver_city(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)  # Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Movie = types.KeyboardButton("/Films_in_Saint_Petersburg")
    Concerts = types.KeyboardButton("/Сoncerts_in_Saint_Petersburg")
    markup.add(Movie, Concerts)  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Отлично, теперь выберите какой тип мероприятий вас интересует", reply_markup=markup)

@bot.message_handler(commands= ['Films_in_Saint_Petersburg'])
def films_in_tver(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши в Санкт-Петербурге", url="https://www.afisha.ru/spb/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/spb/events/movies/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_concerts_Msc = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_films_spb]

    Text_films_spb = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще',
                   '«Афиша» в соц. сетях',
                   'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время',
                   'Рассылка «Афиши»: главные события недели — у вас на почте']

    def remove_common(Text_films_spb, Trach_words):
        for i in Text_films_spb[:]:
            if i in Trach_words:
                Text_films_spb.remove(i)
                Trach_words.remove(i)

    c = remove_common(Text_films_spb, Trach_words)

    for i in Text_films_spb:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это фильмы, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть трейлер прямо на сайте Афиши",reply_markup=markup)  # Возможно эту строку надо перенести в конец
@bot.message_handler(commands= ['Сoncerts_in_Saint_Petersburg'])
def films_in_tver(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши в Санкт-Петербурге", url="https://www.afisha.ru/spb/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/spb/events/concerts/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_concerts_Msc = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_concerts_Msc]

    Text_concerts_spb = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще',
                   '«Афиша» в соц. сетях',
                   'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время',
                   'Рассылка «Афиши»: главные события недели — у вас на почте']

    def remove_common(Text_concerts_spb, Trach_words):
        for i in Text_concerts_spb[:]:
            if i in Trach_words:
                Text_concerts_spb.remove(i)
                Trach_words.remove(i)

    c = remove_common(Text_concerts_spb, Trach_words)
    for i in Text_concerts_spb:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это концерты, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть описание прямо на сайте Афиши", reply_markup=markup)  # Возможно эту строку надо перенести в конец

@bot.message_handler(commands = ['Novosibirsk'])
def tver_city(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)  # Параметры: подстраиваться под размеры = Да, Сколько кнопок в ряде
    Movie = types.KeyboardButton("/Films_in_Novosibirsk")
    Concerts = types.KeyboardButton("/Сoncerts_in_Novosibirsk")
    markup.add(Movie, Concerts)  # Текст Кнопки и адрес ссылки
    bot.send_message(message.chat.id, "Отлично, теперь выберите какой тип мероприятий вас интересует", reply_markup=markup)

@bot.message_handler(commands= ['Films_in_Novosibirsk'])
def films_in_tver(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши в Новосибирске", url="https://www.afisha.ru/novosibirsk/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/novosibirsk/events/movies/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_films_Novosibirsk = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_concerts_Msc]

    Text_concerts_Msc = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще',
                   '«Афиша» в соц. сетях',
                   'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время',
                   'Рассылка «Афиши»: главные события недели — у вас на почте']

    def remove_common(Text_concerts_Msc, Trach_words):
        for i in Text_concerts_Msc[:]:
            if i in Trach_words:
                Text_concerts_Msc.remove(i)
                Trach_words.remove(i)

    c = remove_common(Text_concerts_Msc, Trach_words)

    for i in Text_for_films:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это фильмы, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть трейлер прямо на сайте Афиши",reply_markup=markup)  # Возможно эту строку надо перенести в конец
@bot.message_handler(commands= ['Сoncerts_in_Novosibirsk'])
def films_in_tver(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт Афиши в Новосибирске", url="https://www.afisha.ru/novosibirsk/"))# Текст Кнопки и адрес ссылки
    URL = "https://www.afisha.ru/novosibirsk/events/concerts/"

    def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')  # Парсинг
        Text_for_concerts = soup.find_all('div', class_="mQ7Bh")
        return [c.text for c in Text_for_concerts]

    Text_for_concerts = parser(URL)
    Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще', '«Афиша» в соц. сетях', 'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время', 'Рассылка «Афиши»: главные события недели — у вас на почте']
    if Text_for_concerts in Trach_words:
        del Text_for_concerts[Text_for_concerts.index(Trach_words)]

    for i in Text_for_concerts:
        bot.send_message(message.chat.id, i , parse_mode="html")#Сделать цикл для отправки сообщений

    bot.send_message(message.chat.id, " Это концерты, которые идут в вашем городе прямо сейчас\n"
                                      "Вы можете купить билеты или посмотреть описание прямо на сайте Афиши", reply_markup=markup)  # Возможно эту строку надо перенести в конец
@bot.message_handler()
def get_user_text(message):
    #bot.send_message(message.chat.id, message, parse_mode="html")
    if message.text.lower == "Привет" or "Hi" or "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode="html")
    elif message.text.lower == "id":# Выводится вся информация из message (Нужно потом удалить)
        bot.send_message(message.chat.id, f"Твой id:{message.from_user.id}", parse_mode="html")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode="html")

bot.polling(none_stop=True)