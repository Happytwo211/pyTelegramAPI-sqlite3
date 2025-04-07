import sqlite3


connection = sqlite3.connect('users_data.sqlite3', check_same_thread=False)
cursor = connection.cursor()

#
# cursor.execute(
#     '''
#     CREATE TABLE users_data (
#     user_name TEXT NOT NULL,
#     departure_city TEXT NOT NULL,
#     arrive_city TEXT NOT NULL,
#     adult_persons TEXT NOT NULL,
#     children TEXT NOT NULL,
#     stars TEXT NOT NULL,
#     eat_plan TEXT NOT NULL,
#     days TEXT NOT NULL,
#     period TEXT NOT NULL,
#     user_tg TEXT ,
#     user_whatsapp TEXT ,
#     user_phone TEXT
#     )
#     '''
# )

connection.commit()
connection.close()