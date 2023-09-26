from sqlite3 import Cursor

import requests
import telebot
import random
import sqlite3 as sq

con = sq.connect("saber.db",check_same_thread=False)
cur: Cursor = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    proname TEXT,
    old INTEGER,
    phone_number INTEGER,
    adress TEXT
)""")

# cur.execute("""INSERT INTO users(name,proname,old,phone_number,adress)
# VALUES ('Артем','Пархоменко',27,79006501355,'Санкт-Петербург')""")
# #cur.execute("SELECT * FROM users")

API_TOKEN = '6374135776:AAEjQJnGdbvwGwKYjH1oA2J93tV6Kzo__Mc'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    for row in result:
        bot.send_message(message.chat.id,str(row))
    bot.send_message(message.chat.id,"Все записи в телефонном справочнике на данный момент.")


@bot.message_handler(commands=['add'])
def add_person(message):
    list_i = message.text.split()[1:]
    try:
        cur.execute("""INSERT INTO users(name,proname,old,phone_number,adress)
        VALUES (?,?,?,?,?)""",list_i)
        con.commit()
        bot.send_message(message.chat.id,"Запись успешно добавлена в телефонный справочник")
    except:
        bot.send_message(message.chat.id,"Введите данные нового пользователя по примеру:"
                                         "/add Артем Пархоменко 27 79006501355 Санкт-Петербург")


@bot.message_handler(commands=['delete'])
def add_person(message):
    list_i = message.text.split()[1:]
    try:
        cur.execute("""DELETE FROM users WHERE name = ? and proname = ?""",list_i)
        bot.send_message(message.chat.id,"Запись успешно удалена")
    except:
        bot.send_message(message.chat.id, "Формат записи для удаления: /delete Артем Пархоменко")


# @bot.message_handler(commands=['update'])
# def add_person(message):
#     list_i = message.text.split()[1:]
#     list_update = list_i[:2]
#     list_delete = list_i[2:]
    # try:
    # sql1 = ("""UPDATE users SET(?,?)""",list_update)
    # sql2 = ("""WHERE name = ? and proname = ?""",list_delete)
    # cur.execute(sql1+sql2)
    # cur.execute("""UPDATE users SET (?,?) WHERE name  and proname =""",list_i)

    # bot.send_message(message.chat.id,"Запись успешно изменена")
    # except:
    #     bot.send_message(message.chat.id, "Формат записи для удаления: /update Артем Пархоменко Евгений Гайдарович")
@bot.message_handler(commands=['exit'])
def add_person(message):
    bot.send_message(message.chat.id, "Бот завершил свою работу.")
    con.commit()
    con.close()
    bot.polling()
    bot.stop_bot()


@bot.message_handler(commands=['save'])
def add_person(message):
    bot.send_message(message.chat.id, "Таблица с номерами сохранена.")
    con.commit()


bot.message_handler(commands=['help'])
def add_person(message):
    bot.send_message(message.chat.id, "Для того, чтобы бот вывел текущий справочник номеров введите команду /start."
                                      "Для добавления записи используйте команду /add"
                                      "Для удаления записи используйте команду /delete"
                                      "для сохранения таблицы используйте команду /save"
                                      "для закрытия и прекращения работы бота используйте команду /exit")



# print_data_baze()
# con.commit()
# con.close()
bot.polling()