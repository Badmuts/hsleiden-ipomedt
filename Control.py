import RPi.GPIO as GPIO
import time
from Status import *
# This class is to control the step motor.
# It implements 9 methods

class Control:
	# Construct
	def __init__(self):
		GPIO.setmode(GPIO.BCM)

		self.enable_pin = 18
		self.coil_A_1_pin = 4
		self.coil_A_2_pin = 17
		self.coil_B_1_pin = 23
		self.coil_B_2_pin = 24
		self.buttonPin = 7
		self.prev_state = 1

		GPIO.setup(self.enable_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_2_pin, GPIO.OUT)
		GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		GPIO.output(self.enable_pin, 1)

		self.delay = int(25) / 1000.0

	# Home
	def home(self):
		if status.active == False and status.y > 0:
			while True:
				if (self.button_pressed() == False):
					self.up(1)
				else:
					break
			return

	# Down
	def down(self, steps):
		if status.active == False and status.y >= 0:
			status.active = True
			step_counter = 0
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
					step_counter += 1
					print "DOWN: Level up +1"
				else:
					break

			status.y = status.y + step_counter
			GPIO.cleanup()
			status.active = False
			return  
		return "Is active or Y position equals 0"

	# Up
	def up(self, steps):
		print "UP START"
		if status.active == False and status.y > 0:
			print "UP IF"
			status.active = True
			step_counter = 0
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
					step_counter += 1
					print "UP: Level up +1"
				else:
					break
			# self.prev_state = 1
			status.y = status.y - step_counter
			GPIO.cleanup()
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
			if curr_state != self.prev_state and curr_state == 0:
				self.prev_state = curr_state
				return True
			else:
				# self.prev_state = curr_state
				return False
		return
	# XPos
	# YPos
	# AutoOn
	# AutoOff
	# Shutdown
	# Reboot