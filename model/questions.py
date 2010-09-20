import sqlite3


class Question(object):
    def __init__(self, question, answer, category, answer_form="string", answer_data="", guid=""):
        self.guid = guid
        self.question = question
        self.answer = answer
        self.category = category
        self.answer_form = answer_form
        self.answer_data = answer_data

    def answer(self, answer):
        pass


class QuestionStore(object):
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.conn = sqlite3.connect(dbfile)
        self._setup()

    def _setup(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
                                id INT PRIMARY KEY,
                                category TEXT,
                                question_number INT,
                                date_asked TEXT,
                                date_answered TEXT,
                                question TEXT NOT NULL,
                                answer_form TEXT NOT NULL,
                                answer_data TEXT,
                                correct_answer TEXT, NOT NULL,
                                given_answer TEXT,
                                mark INTEGER,
                                working TEXT)""")
            cursor.commit()
        finally:
            cursor.close()

    def store_question(self, question, timestamp):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""INSERT INTO questions
                            (category, question_number, date_asked, question, answer_form, answer_data, correct_answer)
                            VALUES (?, ?, ?, ?, ?, ?, ?)""", ())
        except:
            cursor.roleback()
            raise
        finally:
            cursor.close()

    def load_questions(self, timestamp):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT question, correct_answer, category, answer_form, answer_data  FROM questions WHERE date_asked = ?", (timestamp))
            for data in cursor:
                yield Question(*data)
        except:
            pass
        finally:
            cursor.close()
