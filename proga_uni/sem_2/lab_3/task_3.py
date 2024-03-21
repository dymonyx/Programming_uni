import sqlite3
try:
    connection = sqlite3.connect('music.db')
    cursor = connection.cursor()
    print("База данных создана и успешно подключена к SQLite")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tMusician(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT,
    age INTEGER,
    sex TEXT);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tSongs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    id_Musicians INTEGER);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tComments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text_of_comment TEXT,
    id_Songs INTEGER,
    id_Musicians INTEGER); """)
    cursor.execute("""SELECT id, nickname, age, sex, id.tSongs, name.tSongs, description.tSongs FROM tMusician, tSongs""")
    cursor.execute("""SELECT id, nickname, age, sex, id.tComments, text_of_comment.tComments, id_Songs.tSongs FROM tMusican, tSongs, tComments """)
    cursor.execute("""SELECT id, name, description, id_Musicians, id.tComments, text_of_comment.tComments, id.Songs.tComments FROM tSongs, tComments""")
    connection.commit()