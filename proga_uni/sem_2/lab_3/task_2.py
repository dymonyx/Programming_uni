import sqlite3

countries = [
    ('Canada',),
    ('Georgia',),
    ('France',),
    ('Italy',)
]

# Попытаться открыть соединение к базе
try:
    # осуществить подключение к БД sqlitePy
    connection = sqlite3.connect('country.db')
    # создать курсор для выполнения запросов
    cursor = connection.cursor()
    print("База данных создана и успешно подключена к SQLite")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tCountry(
    number_p_p INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT);""")
    cursor.execute("INSERT INTO tCountry VALUES(NULL, 'Russia')")
    connection.commit()
    cursor.executemany("""INSERT INTO tCountry (country_name) VALUES (?)""", countries)
    connection.commit()
    # вернуть все строки в виде списка
    cursor.execute('SELECT * FROM tCountry')
    rows = cursor.fetchone()
    print(rows)
    rows = cursor.fetchmany(3)
    print(rows)
    record = cursor.fetchall()
    print(record)
    cursor.execute("DROP TABLE IF EXISTS tCountry")
    # закрыть курсор
    cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    # закрыть соединение с базой
    if connection:
        connection.commit()
        connection.close()
        print("Соединение с SQLite закрыто")
