# Testing
import unittest
from challenges.intermediate.two_words_same_letter import two_words_same_letter

class Test(unittest.TestCase):
	def test_true(self):
		self.assertTrue(two_words_same_letter('Lucky Llama'))

	def test_false(self):
		self.assertFalse(two_words_same_letter('Lucky Alpaca'))

	def test_mixed_case(self):
		self.assertTrue(two_words_same_letter('Lucky llama'))

	def test_one_word(self):
		with self.assertRaises(ValueError):
			two_words_same_letter('Lucky')

	def test_three_words(self):
		with self.assertRaises(ValueError):
			two_words_same_letter('Loving lucky llama')

if __name__ == '__main__':
	unittest.main()