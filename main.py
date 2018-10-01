from flask import Flask, url_for, render_template
import random
import utils

puntended = Flask(__name__)
HOST = 'host'
CLIENT = 'play'

@puntended.route("/")
def hello():
    return render_template('index.html')

@puntended.route('/' + HOST)
def host():
    code = utils.generate_roomcode()
    return render_template(HOST + '.html', roomcode = code)

@puntended.route('/' + CLIENT)
def client():
    return render_template(CLIENT + '.html')

if __name__ == "__main__":
    random.seed(1000)
    puntended.run()
