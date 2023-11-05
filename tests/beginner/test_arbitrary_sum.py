# Testing
import unittest
from challenges.beginner.arbitrary_sum import arbitrary_sum

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(arbitrary_sum(1, 2, 3, 4, 5), 15)

	def test_one(self):
		self.assertEqual(arbitrary_sum(1), 1)

	def test_varied(self):
		self.assertEqual(arbitrary_sum(23, 34, 12), 69)

	def test_type_error(self):
		with self.assertRaises(TypeError):
			arbitrary_sum('string')

if __name__ == '__main__':
	unittest.main()