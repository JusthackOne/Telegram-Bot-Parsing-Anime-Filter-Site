import sqlite3 as sq

from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('data.db')
    cur = base.cursor()

    if base:
        print('Data base connected OK!')
    #base.execute('CREATE TABLE IF NOT EXISTS name_table(`id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, `name` varchar(255) NOT NULL)')

