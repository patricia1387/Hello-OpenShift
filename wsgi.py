from flask import *

from config import hi

application = Flask(__name__)

@application.before_request
@application.route("/")
def hello():
    return hi

if __name__ == "__main__":
    application.run()
