class Customer:
	name = ''
	lastName = ''
	age = 0
	def addCart(self):
		print('Added product',self.name,self.lastName,'s Cart')

customer1 = Customer()
customer1.name = 'Surinthon'
customer1.lastName = 'Karawoot'
customer1.addCart()

customer2 = Customer()
customer2.name = 'pearada'
customer2.lastName = 'Karawoot'
customer2.addCart()

customer3 = Customer()
customer3.name = 'Dream'
customer3.lastName = 'Karawoot'
customer3.addCart()

customer4 = Customer()
customer4.name = 'Norapat'
customer4.lastName = 'Karawoot'
customer4.addCart()
