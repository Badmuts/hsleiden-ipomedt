import RPi.GPIO as GPIO
import time
import os
import subprocess
from Status import *
import syslog

# This class is to control the step motor.
# It implements 9 methods

class Control:
	# Construct
	def __init__(self):
		GPIO.setmode(GPIO.BCM)

		self.destruct = True

		self.enable_pin = 19
		self.coil_A_1_pin = 4
		self.coil_A_2_pin = 17
		self.coil_B_1_pin = 23
		self.coil_B_2_pin = 24
		self.buttonPin = 7
		self.button_prev_state = 1
		self.ligth_sensorpin = 18  
		self.light_prev_state = 1 
		self.event = 1

		GPIO.setup(11, GPIO.OUT) ## Setup GPIO pin 7 to OUT
		GPIO.setup(18, GPIO.IN) ## Setup GPIO pin 18 to INPUT
		GPIO.setup(self.ligth_sensorpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		GPIO.setup(self.enable_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_2_pin, GPIO.OUT)
		GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		GPIO.output(self.enable_pin, 1)

		self.delay = int(2.5) / 1000.0

	# Home
	def home(self):
		self.up(10000)
		return

	def checkLight(self):
		
		light_status = True
		while light_status:
			curr_state = GPIO.input(self.ligth_sensorpin)
			if (curr_state != self.light_prev_state): 
				if (curr_state == 1): 
					event = "FAAAAL"
					print event  
				else:   
					self.animate()
					break
				self.light_prev_state = curr_state 
			time.sleep(0.02)		
		GPIO.cleanup()
		return

	def animate(self):
		while True:
			if (self.destruct == True):
				self.down(100)
				GPIO.output(11, True)
				time.sleep(0.1)
				GPIO.output(11, False)
				self.down(800)
				self.up(750)
			else:
				break
		return

	# Down
	def down(self, steps):
		if status.active == False:
			status.active = True
			# step_counter = 0
			for i in range(0, steps):
				if self.button_pressed() == False:
					self.setStep(1, 0, 0, 0)
					time.sleep(self.delay)
					self.setStep(0, 1, 0, 0)
					time.sleep(self.delay)
					self.setStep(0, 0, 1, 0)
					time.sleep(self.delay)
					self.setStep(0, 0, 0, 1)
					time.sleep(self.delay)
					# step_counter += 1
				else:
					for i in range(0, 5):
						self.setStep(1, 0, 0, 0)
						time.sleep(self.delay)
						self.setStep(0, 1, 0, 0)
						time.sleep(self.delay)
						self.setStep(0, 0, 1, 0)
						time.sleep(self.delay)
						self.setStep(0, 0, 0, 1)
						time.sleep(self.delay)
						# step_counter += 1
					self.self_destruct()
					break
			# status.y += step_counter
			status.active = False
			return  
		return "Is active or Y position equals 0"

	# Up
	def up(self, steps):
		if status.active == False:
			status.active = True
			# step_counter = 0
			for i in range(0, steps):
				if self.button_pressed() == False:
					self.setStep(0, 0, 0, 1) 
					time.sleep(self.delay)
					self.setStep(0, 0, 1, 0)
					time.sleep(self.delay)
					self.setStep(0, 1, 0, 0)
					time.sleep(self.delay)
					self.setStep(1, 0, 0, 0)
					time.sleep(self.delay)
					# step_counter += 1
				else:
					for i in range(0, 5):
						self.setStep(1, 0, 0, 0)
						time.sleep(self.delay)
						self.setStep(0, 1, 0, 0)
						time.sleep(self.delay)
						self.setStep(0, 0, 1, 0)
						time.sleep(self.delay)
						self.setStep(0, 0, 0, 1)
						time.sleep(self.delay)
						# step_counter += 1
					self.self_destruct()
					break
			# status.y -= step_counter
			status.active = False
			return
		return "Is active or Y position equals 0"

	def setStep(self, w1, w2, w3, w4):
		GPIO.output(self.coil_A_1_pin, w1)
		GPIO.output(self.coil_A_2_pin, w2)
		GPIO.output(self.coil_B_1_pin, w3)
		GPIO.output(self.coil_B_2_pin, w4)

	# stop
	def button_pressed(self):
		if status.active == True:
			curr_state = GPIO.input(self.buttonPin)
			if curr_state != self.button_prev_state and curr_state == 0:
				self.button_prev_state = curr_state
				return True
			else:
				# self.button_prev_state = curr_state
				return False
		return
	
	# XPos
	def x_pos(self):
		x = open('/boot/x.txt', 'r')
		value = x.read()
		x.close()
		return value
	# YPos
	def y_pos(self):
		y = open('/boot/y.txt', 'r')
		value = y.read()
		y.close()
		return value
                
	# AutoOff
	# Reboot
	def reboot(self):
		command = "/usr/bin/sudo /sbin/shutdown -r now"
		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]
		print output
		return

	# Shutdown
	def shutdown(self):
		command = "/usr/bin/sudo /sbin/shutdown -h 0"
		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]
		print output
		return

	def self_destruct(self):
		syslog.syslog("DAAN: SELF DESTRUCT")
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(11, GPIO.OUT) ## Setup GPIO pin 7 to OUT
		GPIO.setup(18, GPIO.IN) ## Setup GPIO pin 18 to INPUT
		GPIO.setup(self.ligth_sensorpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		GPIO.setup(self.enable_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_2_pin, GPIO.OUT)
		GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		GPIO.output(self.enable_pin, 1)
		self.destruct = False
		return