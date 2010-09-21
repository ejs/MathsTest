import bottle
from bottle import Bottle, run
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
    return "You've passed"


run(app=myapp, host='localhost', port=8080)
