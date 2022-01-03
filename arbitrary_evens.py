# Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.

def myfunc(*nums):
	evens = []
	for num in nums:
		# % takes the modulus (aka remainder) of a division problem
		# even numbers are divisible by 2, meaning the remainder will be 0
		if num % 2 == 0:
			evens.append(num)
	return evens

# Testing
import unittest

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(myfunc(1, 2, 3, 4, 5, 6), [2, 4, 6])

	def test_evens(self):
		self.assertEqual(myfunc(1, 3, 5), [])

	def test_empty(self):
		self.assertEqual(myfunc(), [])

	def test_type_error(self):
		with self.assertRaises(TypeError):
			myfunc(1, 'string')

if __name__ == '__main__':
	unittest.main()