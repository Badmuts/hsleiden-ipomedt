from flask import Flask, request
from Home import Home
from Control import Control
from Status import *
import syslog
# import logging
# from logging.handlers import FileHandler

app = Flask(__name__)
# Return ball to home

# file_handler = FileHandler('/boot/logger.log')
# file_handler.setLevel(logging.WARNING)
# app.logger.addHandler(file_handler)

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
	# app.logger.warning('Status Y is (%d Y)', status.y)
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
def xpos():
	control = Control()
	return  control.x_pos()

@app.route('/ypos')
def ypos():
	control = Control()
	return control.y_pos()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
