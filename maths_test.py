import bottle
from bottle import Bottle, run, view
from lib.quizz_master import generate_quizz


bottle.debug(True)
myapp = Bottle()


@myapp.route('/')
@myapp.route('/maths')
@view("questions")
def hello():
    return {"questions":generate_quizz()}


@myapp.post('/maths')
def hello():
    return "You've passed"


run(app=myapp, host='localhost', port=8080)
