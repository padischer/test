
class Car(object):

	speed = 0

	def status(self):
		print("%s kmh" % (self.speed))

	def setSpeed(self, speed):
		self.speed = speed




car = Car()

car.status()
car.setSpeed(50)
car.status()

car.setSpeed(0)
car.status()