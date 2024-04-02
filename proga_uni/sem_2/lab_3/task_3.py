import sqlite3

musicians = [("Twenty One pilots", 36, "man"), ("GONE.Fludd", 24, "man"), ("Noize MC", 39, "man"),
             ("Grimes", 27, "woman"), ("Turbowolf", 35, "man")]
songs = [("ГОРОД", "remake к БРАТ 2", 2), ("Overcompenste", "Clancy album", 1),
         ("No no no", "The Free Life album", 5), ("Вселенная бесконечна", "в клипе присутствует ИТМО", 3),
         ("Genesis", "очень красивая песня", 4)]
comments = [("NEW ERA YEAAAAA!1!", 2, 1), ("Посмотрю фильм только ради этой песни в исполнении флады", 1, 2),
            ("МОЙ УНИК В КЛИПЕ НОЙЗА ЛОЛ!!", 4, 3), ("Раньше было лучше..", 5, 4),
            ("hiatus =C", 3, 5)]

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
    id_Musician INTEGER,
    FOREIGN KEY (id_Musician) REFERENCES tMusician(id) ON DELETE CASCADE);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tComments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text_of_comment TEXT,
    id_Songs INTEGER,
    id_Musician INTEGER,
    FOREIGN KEY (id_Songs) REFERENCES tSongs(id) ON DELETE CASCADE,
    FOREIGN KEY (id_Musician) REFERENCES tMusician(id) ON DELETE CASCADE); """)
    cursor.executemany('''INSERT INTO tMusician(nickname, age, sex) VALUES (?, ?, ?)''', musicians)
    cursor.executemany('''INSERT INTO tSongs(name, description, id_Musician) VALUES (?, ?, ?)''', songs)
    cursor.executemany('''INSERT INTO tComments(text_of_comment, id_Songs, id_Musician) VALUES (?, ?, ?)''', comments)
    connection.commit()

    cursor.execute(
        'SELECT tMusician.nickname, tSongs.name, tComments.text_of_comment FROM tMusician, tSongs, tComments WHERE tSongs.id_Musician = tMusician.id AND tComments.id_Musician = tMusician.id AND tComments.id_Songs = tSongs.id')
    rows = cursor.fetchone()
    print(rows)
    rows = cursor.fetchmany(2)
    print(rows)
    record = cursor.fetchall()
    print(record)

    cursor.execute("DROP TABLE IF EXISTS tMusician")
    cursor.execute("DROP TABLE IF EXISTS tSongs")
    cursor.execute("DROP TABLE IF EXISTS tComments")
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
