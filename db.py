import sqlite3

class Sqlite:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT or IGNORE INTO 'users' VALUES (?)",(user_id,))

    def add_photo(self, msg_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'id' VALUES (?)",(msg_id,))

    def get_first(self):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM 'id'""").fetchone()

    def get_user(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'users'").fetchall()

    def delete(self, photo_id):
        with self.connection:
            return self.cursor.execute("""DELETE  FROM 'id' WHERE id = ?""",(str(photo_id),))

    def get_user(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'users'").fetchall()
