# Testing
import unittest
from challenges.beginner.arbitrary_evens import arbitrary_evens

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(arbitrary_evens(1, 2, 3, 4, 5, 6), [2, 4, 6])

	def test_evens(self):
		self.assertEqual(arbitrary_evens(1, 3, 5), [])

	def test_empty(self):
		self.assertEqual(arbitrary_evens(), [])

	def test_type_error(self):
		with self.assertRaises(TypeError):
			arbitrary_evens(1, 'string')

if __name__ == '__main__':
	unittest.main()