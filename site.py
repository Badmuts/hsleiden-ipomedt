from flask import Flask, request
from Home import Home
from Control import Control
from Status import *
import os

app = Flask(__name__)
# Return ball to home

@app.route('/up')
def beam_me_up():
	control = Control()
	if request.args['steps']:
		steps = int(request.args['steps'])
	if steps > 0:
		control.up(steps)
	else:
		control.up(1)
	return "Beam me up Scotty!"

@app.route('/down')
def gtfo():
	control = Control()
	if request.args['steps']:
		steps = int(request.args['steps'])
	if steps > 0:
		control.down(steps)
	else:
		control.down(1)
	return "PUT THAT COOKIE DOWN! NOW!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
