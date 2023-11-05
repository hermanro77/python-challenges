# Testing
import unittest
from challenges.expert.summer_69 import summer_69

class Test(unittest.TestCase):
	def test_normal(self):
		self.assertEqual(summer_69([1, 3, 5]), 9)

	def test_gap(self):
		self.assertEqual(summer_69([4, 5, 6, 7, 8, 9]), 9)

	def test_empty_gap(self):
		self.assertEqual(summer_69([2, 1, 6, 9, 11]), 14)

	def test_two_nines(self):
		self.assertEqual(summer_69([2, 1, 6, 9, 9, 11]), 23)

	def test_empty(self):
		self.assertEqual(summer_69([6, 1, 9]), 0)

	def test_empty_input(self):
		self.assertEqual(summer_69([]), 0)

if __name__ == '__main__':
	unittest.main()