import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('nexaris.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

        def create_tables(self):
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS guilds (
            guild_id INTEGER PRIMARY KEY,
            prefix TEXT,
            language TEXT
        )''')
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            guild_id INTEGER,
            xp INTEGER,
            balance INTEGER,
            FOREIGN KEY(guild_id) REFERENCES guilds(guild_id)
        )''')
            self.conn.commit()

            def get_guild_config(self, guild_id):
                self.cursor.execute('SELECT * FROM guilds WHERE guild_id = ?', (guild_id,))
                return self.cursor.fetchone()

                def set_guild_config(self, guild_id, prefix, language):
                    self.cursor.execute('''INSERT OR REPLACE INTO guilds (guild_id, prefix, language) 
            VALUES (?, ?, ?)''', (guild_id, prefix, language))
                    self.conn.commit()

                    def get_user_data(self, user_id, guild_id):
                        self.cursor.execute('SELECT * FROM users WHERE user_id = ? AND guild_id = ?', (user_id, guild_id))
                        return self.cursor.fetchone()

                        def set_user_data(self, user_id, guild_id, xp, balance):
                            self.cursor.execute('''INSERT OR REPLACE INTO users (user_id, guild_id, xp, balance) 
            VALUES (?, ?, ?, ?)''', (user_id, guild_id, xp, balance))
                            self.conn.commit()
