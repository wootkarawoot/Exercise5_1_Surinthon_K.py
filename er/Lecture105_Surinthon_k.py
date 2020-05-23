class vehicle:
	licenseCode = ''
	serialCode = ''
	face = ''
	
	def trunOnAirConditioner(self):
		print('Trun On : Air')

class Car (vehicle):
	def sayHello():
		print('Hello world')
	
	
class van (vehicle):
	pass
	
class pickUp (vehicle):
	pass
	
class estateCar (vehicle):
	pass
	
	
car1 = Car()
car1.trunOnAirConditioner()

van1 = van()
van1.trunOnAirConditioner()

pickUp1 = pickUp()
pickUp1.trunOnAirConditioner()

estateCar1 = estateCar()
estateCar1.trunOnAirConditioner()
