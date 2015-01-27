from flask import Flask
from Home import Home
from Control import Control

app = Flask(__name__)

@app.route('/up')
def beam_me_up():
	control = Control()
	control.up(36)
	return "Beam me up Scotty!"

@app.route('/down')
def gtfo():
	controlDown = Control()
	controlDown.down(36)
	return "GTFO!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
