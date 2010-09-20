import bottle
from bottle import Bottle, run
from genshi.template import TemplateLoader
from lib.quizz_master import generate_quizz


loader = TemplateLoader(['views'], auto_reload=True)
bottle.debug(True)
myapp = Bottle()


@myapp.route('/')
@myapp.route('/maths')
def hello():
    return loader.load("questions.gen").generate(questions=generate_quizz()).render('html', doctype="html5")


@myapp.post('/maths')
def hello():
    return "You've passed"


run(app=myapp, host='localhost', port=8080)
