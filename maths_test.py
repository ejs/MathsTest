from bottle import Bottle, run, view


myapp = Bottle()


@myapp.route('/')
@myapp.route('/maths')
@view("mainpage")
def hello():
    return {"message":"welcome to maths"}


@myapp.post('/maths')
def hello(name):
    return "You've passed"


run(app=myapp, host='localhost', port=8080)
