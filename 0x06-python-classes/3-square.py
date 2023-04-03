#!/usr/bin/python3

class Square:
	"""Create a class Square with a size attribute"""
	
	def __init__(self, size=0):
		if type(size) is not int:
			raise TypeError("size must be integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size
	def area(self):
		"""Returns surrent square area"""
		return (self.__size **2)
