import sqlite3
import datetime

connection = sqlite3.connect("led_taster.db")
c = connection.cursor()
on_off = False
zeitpunkt = datetime.now

c.execute("""CREATE TABLE IF NOT EXISTS led_status
            (
                id INTEGER PRIMARY KEY,
                led_status BOOLEAN,
                zeitstempel DATETIME
            )""")

c.execute("INSERT INTO led_status (led_status, zeitstempel) values (?,?)",
        (on_off, zeitpunkt))

connection.commit()
connection.close()