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
        'Все включено', callback_data='all_inclusive'
    )
    dinner_quantity_button_2 = types.InlineKeyboardButton(
        'Завтрак', callback_data='breakfast'
    )
    dinner_quantity_button_3 = types.InlineKeyboardButton(
        'Завтрак и ужин', callback_data='br_and_dinner'
    )
    dinner_quantity_button_4 = types.InlineKeyboardButton(
        'Завтрак, обед и ужин', callback_data='every_food'
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
    period_button_1 = types.InlineKeyboardButton(
        'Январь-февраль', callback_data='янв-фев'
    )
    period_button_2 = types.InlineKeyboardButton(
        'Март-Май', callback_data='март-май'
    )
    period_button_3 = types.InlineKeyboardButton(
        'Июнь-август', callback_data='июнь-август'
    )
    period_button_4 = types.InlineKeyboardButton(
        'Сентябрь-октябрь', callback_data='сент-окт'
    )
    period_button_5 = types.InlineKeyboardButton(
        'Ноябрь-Декабрь', callback_data='ноябрь-дек'
    )
    period_button_6 = types.InlineKeyboardButton(
        'Назад', callback_data='main_menu_period'
    )
    period.add(period_button_1,period_button_2,period_button_3,
               period_button_4,period_button_5, period_button_6)
    return period