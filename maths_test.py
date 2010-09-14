import bottle
from bottle import Bottle, run, view
from lib.question_generator import generate_question, describe_category


bottle.debug(True)
myapp = Bottle()


@myapp.route('/')
@myapp.route('/maths')
@view("questions")
def hello():
    questions = {}
    for i in range(5):
        questions["0:{}".format(i)] = generate_question("0")[0]
    for i in range(5):
        questions["0a:{}".format(i)] = generate_question("0a")[0]
    return {"questions":questions}


@myapp.post('/maths')
def hello():
    return "You've passed"


run(app=myapp, host='localhost', port=8080)
