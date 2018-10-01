from flask import Flask

puntended = Flask(__name__)

@puntended.route("/")
def hello():
	return "Helloooo"

@puntended.route("/host")
def host():
	return 'You are hosting the game <input type="submit" name="submit_button" value="Do Something">'
'''
@puntended.route("/play")
def host():
	return "You are playing the game"
'''
if __name__ == "__main__":
	puntended.run()
