from flask import *


application = Flask(__name__)

@application.route("/")
def hello():
    g.greet = 'greetings'
    return Flask

if __name__ == "__main__":
    application.run()
