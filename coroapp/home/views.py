from . import home

@home.route('/')
def homepage():

    return "Welcome to HomePage"