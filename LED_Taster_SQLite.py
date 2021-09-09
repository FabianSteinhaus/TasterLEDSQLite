import sqlite3
import datetime

connection = sqlite3.connect("led_taster.db")
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS led_status
            (
                id INTEGER PRIMARY KEY,
                led_status BOOLEAN,
                zeitstempel DATETIME
            )""")

            
connection.commit()
connection.close()