import sqlite3


connection = sqlite3.connect('data/users_data.sqlite3', check_same_thread=False)
cursor = connection.cursor()

#
# cursor.execute(
#     '''
#     CREATE TABLE users_consult (
#         user_name TEXT,
#         whatsapp TEXT,
#         telegram TEXT,
#         phone_number TEXT
#     )
#     '''
# )

connection.commit()
connection.close()