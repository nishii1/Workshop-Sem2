
class Parent():
	
	def __init__(self):
		self.value = "This is parent class"
		
	def show(self):
		print(self.value)
		
class Child(Parent):
	
	def __init__(self):
		self.value = "This is child class"
		
	def show(self):
		print(self.value)
		
		
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
