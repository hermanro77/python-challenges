# Testing
import unittest
from challenges.intermediate.has_33 import has_33

class Test(unittest.TestCase):
	def test_true(self):
		self.assertTrue(has_33([1, 3, 3]))

	def test_false(self):
		self.assertFalse(has_33([1, 3, 1, 3]))

	def test_false_2(self):
		self.assertFalse(has_33([3, 1, 3]))

	def test_false_none(self):
		self.assertFalse(has_33([1, 2, 4]))

if __name__ == '__main__':
	unittest.main()