from flask import Flask, request, render_template, url_for
from Home import Home
from Control import Control
from Status import *
import syslog
from flask_request_params import bind_request_params

app = Flask(__name__)
# Return ball to home
autoControl = Control()
app.before_request(bind_request_params)

@app.route('/index.htm')
def index():
	style 		= url_for('static', filename='style.css')
	rangeslider = url_for('static', filename='rangeslider.css')
	jquery 		= url_for('static', filename='js/jquery-1.7.2.min.js')
	rjs 		= url_for('static', filename='js/rangeslider.min.js')
	return render_template('index.html', style=style, rangeslider=rangeslider, jquery=jquery, rjs=rjs)

# @app.route('/down.htm', methods=['GET'])
# def down_steps():
# 	steps = request.params.require('steps')
# 	control = Control()
# 	if steps > 0:
# 		control.down(steps)
# 	return "PUT THAT COOKIE DOWN! NOW!"

@app.route('/down.htm')
def down():
	control = Control()
	try:
		steps = int(request.args['steps'])
	except:
		steps = 1
	control.down(steps)
	return "PUT THAT COOKIE DOWN! NOW!"

# @app.route('/up/<int:steps>')
# def up_steps(steps):
# 	control = Control()
# 	if steps > 0:
# 		control.up(steps)
# 	return "Beam me up Scotty!"

@app.route('/up.htm')
def up():
	control = Control()
	try:
		steps = int(request.args['steps'])
	except:
		steps = 1
	control.up(steps)
	return "Beam me up Scotty!"

@app.route('/home.htm')
def return_to_sender():
	control = Control()
	control.home()
	# app.logger.warning('Status Y is (%d Y)', status.y)
	return "Return to sender"

@app.route('/reboot.htm')
def reboot():
	control = Control()
	control.reboot()
	return 

@app.route('/shutdown.htm')
def shutdown():
	control = Control()
	control.shutdown()
	return 

@app.route('/xpos.htm')
def xpos():
	control = Control()
	return  control.x_pos()

@app.route('/ypos.htm')
def ypos():
	control = Control()
	return control.y_pos()

@app.route('/auto_on.htm')
def auto_on():
	# control = Control()
	autoControl.checkLight()
	return "Kapot NICE !!!"

@app.route('/auto_off.htm')
def auto_off():
	autoControl.self_destruct()
	return "Animation stopped"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)