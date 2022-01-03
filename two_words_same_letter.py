# Write a function that takes in a two word string and returns true if they both start with the same letter, otherwise return false (e.g. "Lucky Llama" returns True). (Hint: Remember the split method)

def myfunc(words):
	# split the two words into separate variables
	word1, word2 = words.split(' ')

	# get the first letter of each string
	# use lowercase as "L" is the same letter as "l"
	return word1[0].lower() == word2[0].lower()

# Testing
import unittest

class Test(unittest.TestCase):
	def test_true(self):
		self.assertEqual(myfunc('Lucky Llama'), True)

	def test_false(self):
		self.assertEqual(myfunc('Lucky Alpaca'), False)

	def test_mixed_case(self):
		self.assertEqual(myfunc('Lucky llama'), True)

	def test_one_word(self):
		with self.assertRaises(ValueError):
			myfunc('Lucky')

	def test_three_words(self):
		with self.assertRaises(ValueError):
			myfunc('Loving lucky llama')

if __name__ == '__main__':
	unittest.main()