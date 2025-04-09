import sqlite3


connection = sqlite3.connect('data/db_ALBA_1.sqlite3', check_same_thread=False)
cursor = connection.cursor()

# #
cursor.execute(
    '''
    CREATE TABLE users_data (
        user_name TEXT,
        departure_city TEXT,
        arrive_city TEXT,
        adult_persons TEXT,
        children TEXT,
        stars TEXT,
        eat_plan TEXT,
        days TEXT,
        period TEXT,
        user_tg TEXT,
        user_whatsapp,
        user_phone

    )
    '''
)

cursor.execute('''
CREATE TABLE users_consult(
    user_name TEXT,
    whatsapp TEXT,
    telegram TEXT,
    phone_number TEXT
    )
''')

connection.commit()
connection.close()