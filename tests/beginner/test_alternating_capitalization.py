# Testing
import unittest
from challenges.beginner.alternating_capitalization import alternating_capitalization

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(alternating_capitalization('worldly'), 'wOrLdLy')

	def test_special_characters(self):
		self.assertEqual(alternating_capitalization('123 !'), '123 !')

	def test_type_error(self):
		with self.assertRaises(TypeError):
			alternating_capitalization(1)

if __name__ == '__main__':
	unittest.main()
