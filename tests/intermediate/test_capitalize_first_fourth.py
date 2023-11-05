# Testing
import unittest
from challenges.intermediate.capitalize_first_fourth import capitalize_first_fourth

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(capitalize_first_fourth('macdonald'), 'MacDonald')

	# Is this the right behavior?
	def test_short(self):
		with self.assertRaises(IndexError):
			capitalize_first_fourth('mac')

if __name__ == '__main__':
	unittest.main()