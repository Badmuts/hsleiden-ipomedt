class Status:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.active = False

	def max_y(self):
		# Het maximale ei gehalte is
		# 1 stapje = 0.30mm
		# max = 3 meter
		max_mm = 3 * 1000
		max_steps = max_mm / 0.30
		return max_steps

	def set_y(self, y):
		self.y = y
		f = open('/boot/y.txt', 'w')
		f.write(str(y))
		f.close()
		return

	def set_x(self, x):
		self.x = x
		f = open('/boot/x.txt', 'w')
		f.write(str(x))
		f.close()
		return

status = Status(1, 5)
