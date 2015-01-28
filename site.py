from flask import Flask, request, render_template, url_for
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

@app.route('/')
def index():
	style = url_for('static', filename='style.css')
	rangeslider = url_for('static', filename='rangeslider.css')
	jquery = url_for('static', filename='js/jquery-1.7.2.min.js')
	rjs = url_for('static', filename='js/rangeslider.min.js')
	return render_template('index.html', style=style, rangeslider=rangeslider, jquery=jquery, rjs=rjs)

# @app.route('/up')
# def beam_me_up():
# 	control = Control()
# 	if request.args['steps']:
# 		steps = int(request.args['steps'])
# 	if steps > 0:
# 		control.up(steps)
# 	else:
# 		control.up(1)
# 	return "Beam me up Scotty!"

@app.route('/down/<int:steps>')
def down_steps(steps):
	control = Control()
	if steps > 0:
		control.down(steps)
	return "PUT THAT COOKIE DOWN! NOW!"

@app.route('/down')
def down():
	control = Control()
	control.down(1)
	return "PUT THAT COOKIE DOWN! NOW!"

@app.route('/up/<int:steps>')
def up_steps(steps):
	control = Control()
	if steps > 0:
		control.up(steps)
	return "Beam me up Scotty!"

@app.route('/up')
def up():
	control = Control()
	control.up(1)
	return "Beam me up Scotty!"

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
