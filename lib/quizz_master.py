from lib.question_generator import generate_questions
import model.questions


class Quizz(object):
    def __init__(self, timestamp, db):
        self.timestamp = timestamp
        self.db = db
        self.questions = list(self.db.load_questions(timestamp))
        if not self.questions:
            self.questions = generate_quizz()
            for question in self.questions:
                self.db.store_question(question, timestamp)


def generate_quizz():
    questions = {}
    for category in ("0", "0a"):
        questions[category] = list(generate_questions(category, 5))
    return questions


def answer_questions():
    pass
