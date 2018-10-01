from flask import Flask, url_for, render_template

puntended = Flask(__name__)
HOST = 'host'
CLIENT = 'play'

@puntended.route("/")
def hello():
    return render_template('index.html')

@puntended.route('/' + HOST)
def host():
	return render_template(HOST + '.html')

@puntended.route('/' + CLIENT)
def client():
    return render_template(CLIENT + '.html')

if __name__ == "__main__":
	puntended.run()
