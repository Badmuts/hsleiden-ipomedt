import RPi.GPIO as GPIO
import time
# This class is to control the step motor.
# It implements 9 methods

class Control:
	# Construct
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		self.enable_pin = 18
		self.coil_A_1_pin = 4
		self.coil_A_2_pin = 17
		self.coil_B_1_pin = 23
		self.coil_B_2_pin = 24

		GPIO.setup(self.enable_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_2_pin, GPIO.OUT)

		GPIO.output(self.enable_pin, 1)

		self.delay = int(10) / 1000.0

	# Home
	# Down
	def down(self, steps):  
		for i in range(0, steps):
			self.setStep(1, 0, 0, 0)
			time.sleep(self.delay)
			self.setStep(0, 1, 0, 0)
			time.sleep(self.delay)
			self.setStep(0, 0, 1, 0)
			time.sleep(self.delay)
			self.setStep(0, 0, 0, 1)
			time.sleep(self.delay)
		GPIO.cleanup()
		return

	# Up
	def up(self, steps):  
		for i in range(0, steps):
			self.setStep(0, 0, 0, 1)
			time.sleep(self.delay)
			self.setStep(0, 0, 1, 0)
			time.sleep(self.delay)
			self.setStep(0, 1, 0, 0)
			time.sleep(self.delay)
			self.setStep(1, 0, 0, 0)
			time.sleep(self.delay)
		GPIO.cleanup()
		return

	def setStep(self, w1, w2, w3, w4):
		GPIO.output(self.coil_A_1_pin, w1)
		GPIO.output(self.coil_A_2_pin, w2)
		GPIO.output(self.coil_B_1_pin, w3)
		GPIO.output(self.coil_B_2_pin, w4)
	# XPos
	# YPos
	# AutoOn
	# AutoOff
	# Shutdown
	# Reboot