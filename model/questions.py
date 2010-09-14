import sqlite3


class Questions():
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.conn = sqlite3.connect(dbfile)
        self._setup()


    def _setup(self):
        cursor = conn.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
                                id TEXT PRIMARY KEY,
                                category TEXT,
                                date_asked TEXT,
                                question TEXT, NOT NULL,
                                correct_answer TEXT, NOT NULL,
                                given_answer TEXT,
                                mark INTEGER,
                                working TEXT)""")
            cursor.commit()
        finally:
            cursor.close()
