# Testing
import unittest
from challenges.intermediate.even_min_odd_max import even_min_odd_max

class Test(unittest.TestCase):
	def test_evens(self):
		self.assertEqual(even_min_odd_max(2, 4), 2)

	def test_odds(self):
		self.assertEqual(even_min_odd_max(1, 3), 3)

	def test_mixed(self):
		self.assertEqual(even_min_odd_max(1, 2), 2)

	def test_equal_evens(self):
		self.assertEqual(even_min_odd_max(2, 2), 2)

	def test_equal_odds(self):
		self.assertEqual(even_min_odd_max(1, 1), 1)

if __name__ == '__main__':
	unittest.main()