import telebot
import sqlite3
from keyboards import (start_keyboard, departure_cities_keyboard, arrival_cities_keyboard, adult_tourists, kids_tourists,
                       stars_hotel, dinner_quantity, days_long, peiod, yes_or_no_keyboard,
                       user_contancts, get_phone)
from token_ import TOKEN

connection = sqlite3.connect('users_data.sqlite3', check_same_thread=False)
cursor = connection.cursor()


bot = telebot.TeleBot(TOKEN)

user_data = []


#commands
@bot.message_handler(commands=['start'])
def handle_start(message):

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}'
                                      f'\nЭтот бот поможет тебе подобрать тебе тур!', reply_markup=start_keyboard())
    global user_name
    user_name = message.from_user.first_name
    return user_name

#calldata
@bot.callback_query_handler(func=lambda call: call.data in ['get_tour'])
def handle_callback_get_tour(call):
    message = call.message
    bot.send_message(message.chat.id, f'Ваш город вылета?'
                                      f'\n█▒▒▒▒▒▒▒▒▒ 12%', reply_markup=departure_cities_keyboard())


#CALLBACK_DEPARTURE_CITIES
@bot.callback_query_handler(func=lambda call: call.data in ['Москва', 'Санкт-Петербург', 'Екатеренбург',
                                                            'Новосибирск', 'Казань', 'Другое'])
def handle_callback_cities(call):
    bot.edit_message_text(
        f'В какой стране вы хотите отдохнуть? \n ██▒▒▒▒▒▒▒▒ 25%',
        call.message.chat.id, call.message.message_id, reply_markup=arrival_cities_keyboard()
    )
    global departure_city
    departure_city = call.data
    user_data.append(f'Город вылета - {departure_city}')
    return departure_city


@bot.callback_query_handler(func=lambda call: call.data in ['main_menu_arrival_cities'])
def handle_callback_departure_main_menu_(call):
    bot.edit_message_text(
        f'Ваш город вылета?'
        f'\n█▒▒▒▒▒▒▒▒▒ 12%', call.message.chat.id, call.message.message_id,
        reply_markup=departure_cities_keyboard()
    )
    try:
        user_data.pop()
    except IndexError:
        pass

#CALLDATA_ARRIVAL_CITIES
@bot.callback_query_handler(func=lambda call: call.data in ['Турция', 'Египет', 'ОАЭ',
                                                            'Россия', 'Таиланд', 'Китай',
                                                            'Мальдивы', 'Сейшелы'])
def handle_callback_arrival_cities(call):
    bot.edit_message_text(
        'Выберите количество взрослых туристов\n███▒▒▒▒▒▒▒ 38%',
        call.message.chat.id, call.message.message_id, reply_markup=adult_tourists()

    )
    global arrive_city
    arrive_city = call.data
    user_data.append(f'Город прилета  -{arrive_city}')
    return arrive_city

@bot.callback_query_handler(func=lambda call: call.data in ['main_menu_adult_tourist'])
def handle_main_menu_adult_tourist(call):
    bot.edit_message_text(
        f'В какой стране вы хотите отдохнуть? \n ██▒▒▒▒▒▒▒▒ 25%',
        call.message.chat.id, call.message.message_id, reply_markup=arrival_cities_keyboard()
    )
    try:
        user_data.pop()
    except IndexError:
        pass


#CALLBACK_ADULTS_TOURIST
@bot.callback_query_handler(func=lambda call: call.data in ['👤', '👤👤', '👤👤👤', '👤👤👤👤', '👤👤👤👤👤', 'Другое количество' ])
def handle_adult_tourist(call):
    bot.edit_message_text(
        'Выберите количество детей\n█████▒▒▒▒▒ 50%',
        call.message.chat.id, call.message.message_id, reply_markup=kids_tourists()

    )
    adult_persons = call.data
    user_data.append(f'Количество взрослых - {adult_persons}')
    return adult_persons

@bot.callback_query_handler(func=lambda call: call.data in ['main_menu_kids_tourist'])
def handle_main_menu_adult_tourist(call):
    bot.edit_message_text(
        'Выберите количество взрослых туристов\n███▒▒▒▒▒▒▒ 38%',
        call.message.chat.id, call.message.message_id, reply_markup=adult_tourists()

    )
    try:
        user_data.pop()
    except IndexError:
        pass



#CALLBACK_KIDS_TOURIST
@bot.callback_query_handler(func=lambda call: call.data in ['👶', '👶👶', '👶👶👶', '👶👶👶👶', 'без детей', 'Другое количество дети' ])
def handle_adult_tourist(call):
    bot.edit_message_text(
        'Выберите количество звезд отеля\n██████▒▒▒▒ 62%',
        call.message.chat.id, call.message.message_id, reply_markup=stars_hotel()

    )
    children = call.data
    user_data.append(f'Количесвто детей - {children}')
    return children

@bot.callback_query_handler(func=lambda call: call.data in ['main_menu_stars_hotel'])
def handle_adult_tourist(call):
    bot.edit_message_text(
        'Выберите количество детей\n█████▒▒▒▒▒ 50%',
        call.message.chat.id, call.message.message_id, reply_markup=kids_tourists()

    )
    try:
        user_data.pop()
    except IndexError:
        pass

#CALLBACK_DINERS
@bot.callback_query_handler(func=lambda call: call.data in ['⭐️', '⭐️⭐️', '⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️⭐️'])
def handle_adult_tourist(call):
    bot.edit_message_text(
        'Выберите план питания \n███████▒▒▒ 75%',
        call.message.chat.id, call.message.message_id, reply_markup=dinner_quantity()

    )
    stars = call.data
    user_data.append(f'Количесвто звезд - {stars}')
    return stars

@bot.callback_query_handler(func=lambda call: call.data in ['main_menu_dinner'])
def handle_adult_tourist(call):
    bot.edit_message_text(
        'Выберите количество звезд отеля\n██████▒▒▒▒ 62%',
        call.message.chat.id, call.message.message_id, reply_markup=stars_hotel()

    )
    try:
        user_data.pop()
    except IndexError:
        pass


#CAllBACK DINERS

@bot.callback_query_handler(func=lambda call: call.data in ['Все включено', 'Завтрак', 'Завтрак и ужин', 'Завтрак, обед и ужин'])
def handle_days_long(call):
    bot.edit_message_text(
        'Выберите количесвто дней\n█████████▒  88%',
        call.message.chat.id, call.message.message_id, reply_markup=days_long()

    )
    eat_plan = call.data
    user_data.append(f'План питания -{eat_plan}')
    return eat_plan

@bot.callback_query_handler(func=lambda call: call.data in ['main_menu_days_long'])
def handle_adult_tourist(call):
    bot.edit_message_text(
        'Выберите план питания \n███████▒▒▒ 75%',
        call.message.chat.id, call.message.message_id, reply_markup=dinner_quantity()

    )
    try:
        user_data.pop()
    except IndexError:
        pass


#CALLBACK DAYS LONG
@bot.callback_query_handler(func=lambda call: call.data in ['7-9', '10-12','13-15'])
def handle_days_long(call):
    bot.edit_message_text(
        'В какой период вы планируете поездку?\n██████████ 100%',
        call.message.chat.id, call.message.message_id, reply_markup=peiod()

    )
    days = call.data
    user_data.append(f'Количесвто дней -{days}')
    return days

@bot.callback_query_handler(func=lambda call: call.data in ['main_menu_days_long'])
def handle_days_long(call):
    bot.edit_message_text(
        'Выберите количесвто дней\n█████████▒  88%',
        call.message.chat.id, call.message.message_id, reply_markup=days_long()

    )
    try:
        user_data.pop()
    except IndexError:
        pass

#CALLBACK PEDIOD

@bot.callback_query_handler(func=lambda call: call.data in ['янв-фев', 'март-май','июнь-август', 'сент-окт', 'ноябрь-дек'])
def handle_days_long(call):
    bot.edit_message_text(
        f'Все готово!'
        f'\nПроверте правильность заполненных данных',
        call.message.chat.id, call.message.message_id

    )

    peiod_= call.data
    user_data.append(f'Период отдыха - {peiod_}')


    message = call.message
    for data in user_data:
        bot.send_message(message.chat.id, f'{data}')

    #TEST IS OK#
    cursor.execute('INSERT INTO users_data (user_name, departure_city, arrive_city, '
                   'adult_persons, children, start, eat_plan, days, period) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_name ,departure_city,arrive_city ,
                                                                                                                  'test2','test2','test2',
                                                                                                                  'test','test', peiod_))
    connection.commit()

    # global user_db_data
    # user_db_data = user_data[:]
    user_data.clear()

    bot.send_message(message.chat.id, f'Данные верны?', reply_markup=yes_or_no_keyboard())
    return peiod_
@bot.callback_query_handler(func=lambda call: call.data in ['main_menu_period'])
def handle_days_long(call):
    bot.edit_message_text(
        'В какой период вы планируете поездку?\n██████████ 100%',
        call.message.chat.id, call.message.message_id, reply_markup=peiod()

    )
    try:
        user_data.pop()
    except IndexError:
        pass


@bot.callback_query_handler(func=lambda call: call.data in ['Данные верны'])
def correct(call):
    global message_id
    message_id = bot.edit_message_text(
        'Как можно с вами связаться?',
        call.message.chat.id, call.message.message_id, reply_markup=user_contancts()
    )

@bot.callback_query_handler(func=lambda call: call.data in ['Заполнить заного'])
def incorrect(call):
    message = call.message
    bot.edit_message_text(f'Привет, {message.from_user.first_name}'
                                      f'\nЭтот бот поможет тебе подобрать тебе тур!', call.message.chat.id, call.message.message_id,
                          reply_markup=start_keyboard())



user_tg_contacts=[]

@bot.callback_query_handler(func=lambda call: call.data in ['telegram'])
def telegram(call):
    message = call.message
    bot.edit_message_text( f'Отправте свой ник в телеграм',call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(message, username_tg)





@bot.callback_query_handler(func=lambda call: call.data in ['whatsapp'])
def telegram(call):
    message = call.message
    bot.edit_message_text( f'Отправте свой ник в whatsapp',call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(message, username_whatsapp)


@bot.callback_query_handler(func=lambda call: call.data in ['number'])
def telegram(call):
    message = call.message
    msg = bot.send_message(message.chat.id, f'Введите номер телефона'
                                      f'\nИли поделитесь им через кнопку!', reply_markup=get_phone())

    bot.register_next_step_handler(msg, phone_number)
def phone_number(message):
    bot.send_message(message.chat.id, f'Скоро с вами свяжется специалист по номеру '
                                      f'\n{message.contact.phone_number}')
    # print(message.contact.phone_number)
def username_tg(message):
    user_tg_contacts.append(f'Ник в телеграмме - {message.text}')
    bot.send_message(message.chat.id, f'Специалст свяжется с вами в ближайшее время в телеграм '
                                      f'\n ваш аккаунт-<b>{message.text}</b>', parse_mode='HTML')
    user_tg_contacts.clear()

def username_whatsapp(message):
    user_tg_contacts.append(f'Ник в whatsapp - {message.text}')
    bot.send_message(message.chat.id, f'Специалст свяжется с вами в ближайшее время в whatsapp'
                                      f'\nваш аккаунт-<b>{message.text}</b>', parse_mode='HTML')
    user_tg_contacts.clear()


# connection.commit()
# connection.close()


if __name__ == "__main__":
    bot.polling(none_stop=True)

