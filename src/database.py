import sqlite3
import datetime


DB = Database()

class Database():
    def __init__(self):
        self.create_table()
        
    def conect(self):
        """
        Connect to the database if it exists, if not, create it
        """
        try:
            con = sqlite3.connect('database.db')
            return con
        except Exception as e:
            print(e)
            
    def create_table(self):
        """
        Create the table if it does not exist
        """
        con = self.conect()
        cursor = con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, last_message TEXT, type TEXT, date TEXT)')
        con.commit()
        con.close()
        
    def insert_last_message(self, id, last_message, type):
        con = self.conect()
        cursor = con.cursor()
        if(self.get_user(id) == None): # The user does not exist, create it
            cursor.execute('INSERT INTO users (id, last_message, type, date) VALUES (?, ?, ?, ?)', (id, last_message, type, datetime.datetime.now()))
        else:
            cursor.execute('UPDATE users SET last_message = ?, type = ?, date = ? WHERE id = ?', (last_message, type, datetime.datetime.now(), id))
        con.commit()
        con.close()
        
    def get_user(self, id):
        con = self.conect()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
        user = cursor.fetchone()
        con.close()
        return user

    def get_last_message(self, id):
        con = self.conect()
        cursor = con.cursor()
        cursor.execute('SELECT last_message FROM users WHERE id = ?', (id,))
        last_message = cursor.fetchone()
        con.close()
        return last_message[0]