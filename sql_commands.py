import sqlite3


connection = sqlite3.connect('db3.sqlite3', check_same_thread=False)
cursor = connection.cursor()

#
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
        user_tg TEXT
    )
    '''
)

connection.commit()
connection.close()