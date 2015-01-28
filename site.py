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

@app.route('/home')
def return_to_sender():
	control = Control()
	control.home()
	return "Return to sender"

@app.route('/reboot')
def reboot():
	control = Control()
	control.reboot()
	return 

@app.route('/shutdown')
def shutdown():
	control = Control()
	control.shutdown()
	return 

@app.route('/xpos')
def shutdown():
	control = Control()
	return  control.x_pos()

@app.route('/ypos')
def shutdown():
	control = Control()
	return control.y_pos()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
