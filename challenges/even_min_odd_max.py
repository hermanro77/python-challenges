# Write a function that returns the lesser of two numbers if they are both even, and the greater of two numbers if either are odd. (try the min and max method)

def myfunc(num1, num2):
	if (num1 % 2 == 0) and (num2 % 2 == 0): # both are even
		return min(num1, num2)
	else:
		return max(num1, num2)

# Testing
import unittest

class Test(unittest.TestCase):
	def test_evens(self):
		self.assertEqual(myfunc(2, 4), 2)

	def test_odds(self):
		self.assertEqual(myfunc(1, 3), 3)

	def test_mixed(self):
		self.assertEqual(myfunc(1, 2), 2)

	def test_equal_evens(self):
		self.assertEqual(myfunc(2, 2), 2)

	def test_equal_odds(self):
		self.assertEqual(myfunc(1, 1), 1)

if __name__ == '__main__':
	unittest.main()