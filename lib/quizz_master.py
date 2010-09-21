from lib.question_generator import generate_questions, categories
import model.questions


class Quizz(object):
    def __init__(self, quizzid):
        self.quizzid = quizzid
        self.questions = dict((c, list(generate_questions(c, 5))) for c in categories)

    def answers(self, data):
        for category in self.questions:
            for question in self.questions[category]:
                name = category + ':' + question.guid
                question.answer(data.get(name), data.get('working:'+name))

    def all_answered(self):
        return True
