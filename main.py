from sqlite3 import Cursor

import telebot
import random
import sqlite3 as sq

con = sq.connect("saber.db",check_same_thread=False)
cur: Cursor = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    proname TEXT,
    sex INTEGER,
    old INTEGER,
    phone_number INTEGER,
    adress TEXT
)""")

def print_data_baze():
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
    for row in cur.fetchall():
        print(row)

# cur.execute("""INSERT INTO users(name,proname,sex,old,phone_number,adress)
# VALUES ('Артем','Пархоменко',1,27,79006501355,'Санкт-Петербург')""")
# cur.execute("SELECT * FROM users")

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
    bot.send_message(message.chat.id,"Введите данные нового пользователя по примеру:"
                                     "Артем Пархоменко 1 27 79006501355 Санкт-Петербург")


print_data_baze()
con.commit()
# con.c
# con.close()
bot.polling()