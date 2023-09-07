import telebot
from telebot import types
import datetime
import os
import csv
import time
token = '5914787699:AAEqkorBpJEkDOt0LHbAsI4ycCz_U70Pes0'
bot = telebot.TeleBot(token)
with open('zadachi/zdchi.txt') as f:
    A = f.read().split()

markup = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('НАЗАД')
markup.row(btn1)

markup1 = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('1')
btn2 = types.KeyboardButton('2')
markup1.row(btn1, btn2)
btn3 = types.KeyboardButton('3')
btn4 = types.KeyboardButton('4')
markup1.row(btn3, btn4)
btn5 = types.KeyboardButton('НАЗАД')
markup1.row(btn5)


@bot.message_handler(commands=['start', 'nick'])
def start_message(message):
    bot.send_message(message.chat.id, "Придумайте себе никнейм, который будет отображаться в рейтинге."
                                      " Оскорбительные будут забанены, использовать имена и фамилии можно"
                                      ", но необязательно. Для перезаписи используйте /nick.\nЕсли вы уже создавали ник"
                                      ", то он сохранен нет необходимости создавать новый, нажмите НАЗАД.", reply_markup=markup)
    bot.register_next_step_handler(message, nick)


@bot.message_handler(commands=['contest'])
def contest(message):
    bot.send_message(message.chat.id, text='Для ответа на задачу нажмите на номер', reply_markup=markup1)
    bot.register_next_step_handler(message, click)


def click(message):
    if message.text == '1':
        msg = bot.send_message(message.chat.id, "Ваш ответ на 1 задачу:", reply_markup=markup)
        bot.register_next_step_handler(msg, ans1)
    elif message.text == '2':
        msg = bot.send_message(message.chat.id, "Ваш ответ на 2 задачу:", reply_markup=markup)
        bot.register_next_step_handler(msg, ans2)
    elif message.text == '3':
        msg = bot.send_message(message.chat.id, "Ваш ответ на 3 задачу:", reply_markup=markup)
        bot.register_next_step_handler(msg, ans3)
    elif message.text == '4':
        msg = bot.send_message(message.chat.id, "Ваш ответ на 4 задачу:", reply_markup=markup)
        bot.register_next_step_handler(msg, ans4)
    elif message.text == 'НАЗАД':
        bot.send_message(message.chat.id, "Доступные команды: \n/nick\n/help\n/contest")
    else:
        msg = bot.reply_to(message, "Что-то не так, используйте кнопки")
        bot.register_next_step_handler(msg, click)


@bot.message_handler(commands=['help'])
def help_m(message):
    bot.send_message(message.chat.id, 'Для того, чтобы начать решать задачки используйте /contest\nДля создания или '
                                      'смены ника используйте /nick\nПри  возникновении технических проблем пишите'
                                      ' @raamensavin')


def ans1(message):
    if message.text == 'НАЗАД':
        bot.send_message(message.chat.id, 'Для ответа на задачу нажмите на номер', reply_markup=markup1)
        bot.register_next_step_handler(message, click)
    else:
        with open('ans/z1/zad1.csv', "r") as fin:
            at1 = csv.reader(fin)
            a = 0
            at = []
            for row in at1:
                a += 1
                at += row
        if at.count(message.from_user.username) == 0:
            if message.text == A[1]:
                with open('ans/z1/zad1.csv', "a") as fin:
                    user = [datetime.datetime.now(), time.time(), message.from_user.username, message.from_user.id,
                            message.text]
                    writer = csv.writer(fin)
                    writer.writerow(user)
                bot.send_message(message.chat.id, f"верно, ты сдал задачу {a+1}-м", reply_markup=markup1)
                if a == 0:
                    bot.send_message(chat_id='726382042', text=f"1 задачу сдал верно {message.from_user.username}")
            else:
                with open('ans/z1/wrong_zad1.csv', "a") as fin:
                    user = [datetime.datetime.now(), message.from_user.username, message.from_user.id, message.text]
                    writer = csv.writer(fin)
                    writer.writerow(user)
                bot.send_message(message.chat.id, "неверный ответ", reply_markup=markup1)
        else:
            bot.send_message(message.chat.id, "вы уже сдали эту задачу", reply_markup=markup1)
        bot.register_next_step_handler(message, click)


def ans2(message):
    if message.text == 'НАЗАД':
        bot.send_message(message.chat.id, 'Для ответа на задачу нажмите на номер', reply_markup=markup1)
        bot.register_next_step_handler(message, click)
    else:
        with open('ans/z2/zad2.csv', "r") as fin:
            at1 = csv.reader(fin)
            a = 0
            at = []
            for row in at1:
                a += 1
                at += row
        if at.count(message.from_user.username) == 0:
            if message.text == A[2]:
                with open('ans/z2/zad2.csv', "a") as fin:
                    user = [datetime.datetime.now(), time.time(), message.from_user.username, message.from_user.id,
                            message.text]
                    writer = csv.writer(fin)
                    writer.writerow(user)
                bot.send_message(message.chat.id, f"верно, ты сдал задачу {a+1}-м", reply_markup=markup1)
                if a == 0:
                    bot.send_message(chat_id='726382042', text=f"2 задачу сдал верно {message.from_user.username}")
            else:
                with open('ans/z2/wrong_zad2.csv', "a") as fin:
                    user = [datetime.datetime.now(), message.from_user.username, message.from_user.id, message.text]
                    writer = csv.writer(fin)
                    writer.writerow(user)
                bot.send_message(message.chat.id, "неверный ответ", reply_markup=markup1)
        else:
            bot.send_message(message.chat.id, "вы уже сдали эту задачу", reply_markup=markup1)
        bot.register_next_step_handler(message, click)


def ans3(message):
    if message.text == 'НАЗАД':
        bot.send_message(message.chat.id, 'Для ответа на задачу нажмите на номер', reply_markup=markup1)
        bot.register_next_step_handler(message, click)
    else:
        with open('ans/z3/zad3.csv', "r") as fin:
            at1 = csv.reader(fin)
            a = 0
            at = []
            for row in at1:
                a += 1
                at += row
        if at.count(message.from_user.username) == 0:
            if message.text == A[3]:
                with open('ans/z3/zad3.csv', "a") as fin:
                    user = [datetime.datetime.now(), time.time(), message.from_user.username, message.from_user.id,
                            message.text]
                    writer = csv.writer(fin)
                    writer.writerow(user)
                bot.send_message(message.chat.id, f"верно, ты сдал задачу {a+1}-м", reply_markup=markup1)
                if a == 0:
                    bot.send_message(chat_id='726382042', text=f"3 задачу сдал верно {message.from_user.username}")
            else:
                with open('ans/z3/wrong_zad3.csv', "a") as fin:
                    user = [datetime.datetime.now(), message.from_user.username, message.from_user.id, message.text]
                    writer = csv.writer(fin)
                    writer.writerow(user)
                bot.send_message(message.chat.id, "неверный ответ", reply_markup=markup1)
        else:
            bot.send_message(message.chat.id, "вы уже сдали эту задачу", reply_markup=markup1)
        bot.register_next_step_handler(message, click)


def ans4(message):
    if message.text == 'НАЗАД':
        bot.send_message(message.chat.id, 'Для ответа на задачу нажмите на номер', reply_markup=markup1)
        bot.register_next_step_handler(message, click)
    else:
        with open('ans/z4/zad4.csv', "r") as fin:
            at1 = csv.reader(fin)
            a = 0
            at = []
            for row in at1:
                a += 1
                at += row
        if at.count(message.from_user.username) == 0:
            if message.text == A[4]:
                with open('ans/z4/zad4.csv', "a") as fin:
                    user = [datetime.datetime.now(), time.time(), message.from_user.username, message.from_user.id,
                            message.text]
                    writer = csv.writer(fin)
                    writer.writerow(user)
                bot.send_message(message.chat.id, f"верно, ты сдал задачу {a+1}-м", reply_markup=markup1)
                if a == 0:
                    bot.send_message(chat_id='726382042', text=f"4 задачу сдал верно {message.from_user.username}")
            else:
                with open('ans/z4/wrong_zad4.csv', "a") as fin:
                    user = [datetime.datetime.now(), message.from_user.username, message.from_user.id, message.text]
                    writer = csv.writer(fin)
                    writer.writerow(user)
                bot.send_message(message.chat.id, "неверный ответ", reply_markup=markup1)
        else:
            bot.send_message(message.chat.id, "вы уже сдали эту задачу", reply_markup=markup1)
        bot.register_next_step_handler(message, click)


def nick(message):
    if message.text[0] == '/' or len(message.text) > 30:
        bot.send_message(message.chat.id, "Некорректное имя попробуйте другое")
        bot.register_next_step_handler(message, nick)
    elif message.text == "НАЗАД":
        bot.send_message(message.chat.id, "Доступные команды: \n/nick\n/help\n/contest")
    else:
        a = 0
        with open('nicks.csv', "r") as fin:
            re = csv.reader(fin)
            at = []
            for row in re:
                at += row
            if at.count(message.text) != 0:
                bot.send_message(message.chat.id, "Занят, выберите другой")
                bot.register_next_step_handler(message, nick)
            else:
                a = 1
        if a == 1:
            with open('nicks.csv', "a") as fin:
                writer = csv.writer(fin)
                usr = [message.from_user.id, message.from_user.username, message.text]
                writer.writerow(usr)
                bot.send_message(message.chat.id, f"Очень приятно, {message.text}, для того, чтоб"
                                                  f" получить и начать сдавать задачи напишите /contest")


@bot.message_handler()
def penis(message):
    if message.from_user.username == 'raamensavin' and message.text == 'чистка':
        pipa = '/Users/romansavin/Desktop/progs/booot/chistka.py'
        os.system(f'python3 {pipa}')
    bot.send_message(message.chat.id, "Что-то не так, используйте /help")


bot.infinity_polling()
