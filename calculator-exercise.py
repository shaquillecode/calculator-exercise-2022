import math

class Calculator:

	""" 
	Calculator module for in class assignment 
	"""

	def add(self,x,y):
		""" add's two numbers x,y together """
		return x + y


	def sine(self,x):
		'''Finds the sine of the value passed in'''
		return math.sin(x)

	def cosine(self,x):
		'''Finds the cosine of the value passed in'''
		return math.cos(x)

	def tangent(self,x):
		'''Finds the tangent of the value passed in'''
		return math.tan(x)



if __name__ == '__main__':
	calc = Calculator()
	print(calc.add(2,3))
	print(calc.sine(2))
	print(calc.cosine(2))
	print(calc.tangent(2))