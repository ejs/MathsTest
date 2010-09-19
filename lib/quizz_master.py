from lib.question_generator import generate_questions
import model.questions


class Quizz():
    def __init__(self, guid, date, questions):
        self.guid = guid
        self.date = date
        self.questions = list(questions)


def generate_quizz():
    questions = {}
    for category in ("0", "0a"):
        questions[category] = list(generate_questions(category, 5))
    return questions


def answer_questions():
    pass
