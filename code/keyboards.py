from telebot import types
def start_keyboard():
    start_keyboard = types.InlineKeyboardMarkup()
    start_keyboard_button_1 = types.InlineKeyboardButton(
    'Подобрать Тур', callback_data='get_tour'
    )
    start_keyboard_button_2 = types.InlineKeyboardButton(
    'Получить консультацию', callback_data='get_consult'
    )
    start_keyboard.add(
        start_keyboard_button_1,start_keyboard_button_2
    )
    return start_keyboard

def consult_kb ():
    consult_kb_ = types.InlineKeyboardMarkup()
    consult_kb_b_1 = types.InlineKeyboardButton(
        'По телефону', callback_data='phone_consult'
    )
    consult_kb_b_2 = types.InlineKeyboardButton(
        'По телеграмм', callback_data='telegram_consult'
    )
    consult_kb_.add(consult_kb_b_1,consult_kb_b_2)
    return consult_kb_

def departure_cities_keyboard():
    cities_keyboard = types.InlineKeyboardMarkup()
    cities_keyboard_button_1 = types.InlineKeyboardButton(
        'Москва', callback_data='Москва'
    )
    cities_keyboard_button_2 = types.InlineKeyboardButton(
        'Санкт-Петербург', callback_data='Санкт-Петербург'
    )
    cities_keyboard_button_3 = types.InlineKeyboardButton(
        'Екатеренбург', callback_data='Екатеренбург'
    )
    cities_keyboard_button_4 = types.InlineKeyboardButton(
        'Новосибирск', callback_data='Новосибирск'
    )
    cities_keyboard_button_5 = types.InlineKeyboardButton(
        'Казань', callback_data='Казань'
    )
    cities_keyboard_button_6 = types.InlineKeyboardButton(
        'Другое', callback_data='Другое'
    )

    cities_keyboard.add(
        cities_keyboard_button_1,cities_keyboard_button_2,cities_keyboard_button_3,
        cities_keyboard_button_4,cities_keyboard_button_5,cities_keyboard_button_6
    )
    return cities_keyboard

def arrival_cities_keyboard():
    cities_keyboard = types.InlineKeyboardMarkup()
    cities_keyboard_button_1 = types.InlineKeyboardButton(
        'Турция', callback_data='Турция'
    )
    cities_keyboard_button_2 = types.InlineKeyboardButton(
        'Египет', callback_data='Египет'
    )
    cities_keyboard_button_3 = types.InlineKeyboardButton(
        'ОАЭ', callback_data='ОАЭ'
    )
    cities_keyboard_button_4 = types.InlineKeyboardButton(
        'Россия', callback_data='Россия'
    )
    cities_keyboard_button_5 = types.InlineKeyboardButton(
        'Таиланд', callback_data='Таиланд'
    )
    cities_keyboard_button_6 = types.InlineKeyboardButton(
        'Китай', callback_data='Китай'
    )
    cities_keyboard_button_7 = types.InlineKeyboardButton(
        'Мальдивы', callback_data='Мальдивы'
    )
    cities_keyboard_button_8 = types.InlineKeyboardButton(
        'Сейшелы', callback_data='Сейшелы'
    )
    cities_keyboard_button_9 = types.InlineKeyboardButton(
        'Назад', callback_data='main_menu_arrival_cities'
    )
    cities_keyboard.add(
        cities_keyboard_button_1, cities_keyboard_button_2, cities_keyboard_button_3,
        cities_keyboard_button_4, cities_keyboard_button_5, cities_keyboard_button_6, cities_keyboard_button_7,
        cities_keyboard_button_8, cities_keyboard_button_9
    )
    return cities_keyboard

def adult_tourists():
    adult_tourists = types.InlineKeyboardMarkup(row_width=2)
    adult_tourists_button_1 = types.InlineKeyboardButton(
        '👤', callback_data='👤'
    )
    adult_tourists_button_2 = types.InlineKeyboardButton(
        '👤👤', callback_data='👤👤'
    )
    adult_tourists_button_3 = types.InlineKeyboardButton(
        '👤👤👤', callback_data='👤👤👤'
    )
    adult_tourists_button_4 = types.InlineKeyboardButton(
        '👤👤👤👤', callback_data='👤👤👤👤'
    )
    adult_tourists_button_5 = types.InlineKeyboardButton(
        '👤👤👤👤👤', callback_data='👤👤👤👤👤'
    )
    adult_tourists_button_6 = types.InlineKeyboardButton(
        'Другое количество', callback_data='Другое количество'
    )
    adult_tourists_button_7 = types.InlineKeyboardButton(
        'Назад', callback_data='main_menu_adult_tourist'
    )
    adult_tourists.add(adult_tourists_button_1,adult_tourists_button_2,adult_tourists_button_3,
                       adult_tourists_button_4, adult_tourists_button_5, adult_tourists_button_6, adult_tourists_button_7)
    return adult_tourists

def kids_tourists():
    kids_tourists = types.InlineKeyboardMarkup(row_width=2)
    kids_tourists_button_1 = types.InlineKeyboardButton(
        '👶', callback_data='👶'
    )
    kids_tourists_button_2 = types.InlineKeyboardButton(
        '👶👶', callback_data='👶👶'
    )
    kids_tourists_button_3 = types.InlineKeyboardButton(
        '👶👶👶', callback_data='👶👶👶'
    )
    kids_tourists_button_4 = types.InlineKeyboardButton(
        '👶👶👶👶', callback_data='👶👶👶👶'
    )
    kids_tourists_button_5 = types.InlineKeyboardButton(
        'без детей', callback_data='без детей'
    )
    kids_tourists_button_6 = types.InlineKeyboardButton(
        'Другое количество', callback_data='Другое количество дети'
    )
    kids_tourists_button_7 = types.InlineKeyboardButton(
        'Назад', callback_data='main_menu_kids_tourist'
    )
    kids_tourists.add(kids_tourists_button_1,kids_tourists_button_2,kids_tourists_button_3,
                      kids_tourists_button_4,kids_tourists_button_5,kids_tourists_button_6,kids_tourists_button_7)
    return kids_tourists

def stars_hotel():
    stars_hotel = types.InlineKeyboardMarkup(row_width=2)
    stars_hotel_button_1 = types.InlineKeyboardButton(
        '⭐️', callback_data='⭐️'
    )
    stars_hotel_button_2 = types.InlineKeyboardButton(
        '⭐️⭐️', callback_data='⭐️⭐️'
    )
    stars_hotel_button_3 = types.InlineKeyboardButton(
        '⭐️⭐️⭐️', callback_data='⭐️⭐️⭐️'
    )
    stars_hotel_button_4= types.InlineKeyboardButton(
        '⭐️⭐️⭐️⭐️', callback_data='⭐️⭐️⭐️⭐️'
    )
    stars_hotel_button_5 = types.InlineKeyboardButton(
        '⭐️⭐️⭐️⭐️⭐️', callback_data='⭐️⭐️⭐️⭐️⭐️'
    )
    stars_hotel_button_6 = types.InlineKeyboardButton(
        'Назад', callback_data='main_menu_stars_hotel'
    )
    stars_hotel.add(stars_hotel_button_1,stars_hotel_button_2,stars_hotel_button_3,
                    stars_hotel_button_4, stars_hotel_button_5, stars_hotel_button_6)
    return stars_hotel

def dinner_quantity():
    dinner_quantity = types.InlineKeyboardMarkup()
    dinner_quantity_button_1 = types.InlineKeyboardButton(
        'Все включено', callback_data='Все включено'
    )
    dinner_quantity_button_2 = types.InlineKeyboardButton(
        'Завтрак', callback_data='Завтрак'
    )
    dinner_quantity_button_3 = types.InlineKeyboardButton(
        'Завтрак и ужин', callback_data='Завтрак и ужин'
    )
    dinner_quantity_button_4 = types.InlineKeyboardButton(
        'Завтрак, обед и ужин', callback_data='Завтрак, обед и ужин'
    )
    dinner_quantity_button_5 = types.InlineKeyboardButton(
        'Назад', callback_data='main_menu_dinner'
    )
    dinner_quantity.add(dinner_quantity_button_1,dinner_quantity_button_2,dinner_quantity_button_3,
                        dinner_quantity_button_4,dinner_quantity_button_5)
    return dinner_quantity

def days_long():
    days_long = types.InlineKeyboardMarkup()
    days_long_button_1 = types.InlineKeyboardButton(
        '7-9', callback_data='7-9'
    )
    days_long_button_2 = types.InlineKeyboardButton(
        '10-12', callback_data='10-12'
    )
    days_long_button_3 = types.InlineKeyboardButton(
        '13-15', callback_data='13-15'
    )
    days_long_button_4 = types.InlineKeyboardButton(
        'Назад', callback_data='main_menu_days_long'
    )
    days_long.add(days_long_button_1,days_long_button_2,days_long_button_3,
                  days_long_button_4)
    return days_long

def peiod():
    period = types.InlineKeyboardMarkup()
    period_b_1 = types.InlineKeyboardButton(
        'Январь', callback_data='Январь'
    )
    period_b_2 = types.InlineKeyboardButton(
        'Февраль', callback_data='Февраль'
    )
    period_b_3 = types.InlineKeyboardButton(
        'Март', callback_data='Март'
    )
    period_b_4 = types.InlineKeyboardButton(
        'Апрель', callback_data='Апрель'
    )
    period_b_5 = types.InlineKeyboardButton(
        'Май', callback_data='Май'
    )
    period_b_6 = types.InlineKeyboardButton(
        'Июнь', callback_data='Июнь'
    )
    period_b_7 = types.InlineKeyboardButton(
        'Июль', callback_data='Июль'
    )
    period_b_8 = types.InlineKeyboardButton(
        'Август', callback_data='Август'
    )
    period_b_9 = types.InlineKeyboardButton(
        'Сентябрь', callback_data='Сентябрь'
    )
    period_b_10 = types.InlineKeyboardButton(
        'Октябрь', callback_data='Октябрь'
    )
    period_b_11 = types.InlineKeyboardButton(
        'Ноябрь', callback_data='Ноябрь'
    )
    period_b_12 = types.InlineKeyboardButton(
        'Декабрь', callback_data='Декабрь'
    )
    period.add(period_b_1,period_b_2,period_b_3,period_b_4,period_b_5,
               period_b_6,period_b_7,period_b_8,period_b_9,period_b_10,period_b_11,period_b_12)
    return period

def yes_or_no_keyboard():
    kb = types.InlineKeyboardMarkup()
    kb_button_1 = types.InlineKeyboardButton(
        'Данные верны', callback_data='Данные верны'
    )
    kb_button_2 = types.InlineKeyboardButton(
        'Заполнить заново', callback_data='Заполнить заного'
    )
    kb.add(kb_button_1, kb_button_2)
    return kb

def user_contancts():
    contands_kb = types.InlineKeyboardMarkup(row_width=2)
    contands_kb_button_1 = types.InlineKeyboardButton(
        'Telegram', callback_data='telegram'
    )
    contands_kb_button_2 = types.InlineKeyboardButton(
        'По номеру телефона', callback_data='number'
    )
    contands_kb.add(contands_kb_button_1, contands_kb_button_2)
    return contands_kb

def     get_phone():
    kb_phone = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    kb_phone_button_1 = types.KeyboardButton(
        text='Поделиться номером телефона?', request_contact=True
    )
    kb_phone.add(kb_phone_button_1)
    return kb_phone

