#!/usr/bin/python3

class Square:
	"""Create a class Square with a size attribute"""
	
	def __init__(self, size=0, position=(0,0)):
		"""instantiates attributes size and position"""
		self.__size = size
		self.__position = position

	@property
	def size(self):
		"""get private instance attribute size"""
		return (self.__size)

	@size.setter
	def size(self, value):
		"""sets private instance attribute size"""
		if type(value) is not int:
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	@property
	def position(self):
		"""get private instance attribute position"""
		return (self.__position)
	
	@position.setter
	def postion(self, value):
		"""set private instance attribute position"""
		count = 0
		while 1:
			if type(value) is not tuple or len(value) is not 2:
				count += 1
				break
			if type(value[0]) is not int or type(value[1]) is not int:
				count += 1
				break
			if value[0] < 0 or value[1] < 0:
				check += 1
				break
			if count is 0:
				self.__position = value
			else:
				raise TypeError("position must be a tuple of 2 positive integers")


	def area(self):
		"""Returns current square area"""
		return (self.__size * self.__size)
		

	def my_print(self):
		"""print sqaure of size with character #"""
		if self.__size > 0:
			for i in range(self.__position[1]):
				print()
			for y in range(self.__size):
				for j in range(self.__position[0]):
					print(" ", end='')
				for x in range(self.__size):
					print("#", end='')
				print()
			else:
				print()
			
