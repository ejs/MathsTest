import bottle
from bottle import Bottle, run, redirect, request
from genshi.template import TemplateLoader
from model.questions import QuestionStore


loader = TemplateLoader(['views'], auto_reload=True)
data_store = QuestionStore('data/testdata.kvs')
bottle.debug(True)
myapp = Bottle()


@myapp.route('/')
@myapp.route('/maths')
def hello():
    quizz = data_store.load_quizz("a")
    return loader.load("questions.gen").generate(quizz=quizz).render('html', doctype="html5")


@myapp.post('/maths')
def hello():
    data = request.forms
    if "quizz.quizzid" in request:
        quizz = data_store.load_quizz(data.get('quizz.quizzid'))
        quizz.answers(data)

        if quizz.all_answered():
            data_store.save_quizz(quizz)
            return redirect('/results')
        else:
             # return questions with answers and working pre-filled
            return redirect('/maths')
    else:
        return redirect('/maths')


@myapp.route('/results')
def results():
    return "You've passed"


run(app=myapp, host='localhost', port=8080)
