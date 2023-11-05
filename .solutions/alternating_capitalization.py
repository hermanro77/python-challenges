# Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume only letters, and don't worry about spaces, numbers, or punctuation. You can start with either upper or lowercase, as long as they alternate (ex: worldly become wOrLdLy)

def myfunc(word):
	result = ""
	upper = False

	for letter in word:
		if upper:
			result += letter.upper()
		else:
			result += letter.lower()
		upper = not upper

	return result

# Alternate method
def myfunc_enumerate(word):
	result = ""

	for index, letter in enumerate(word): # enumerate() includes indexes when enumerating
		if index % 2 == 0: # if the index is even
			result += letter.lower()
		else: # if the index is odd
			result += letter.upper()

	return result

# Testing
import unittest

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(myfunc('worldly'), 'wOrLdLy')

	def test_special_characters(self):
		self.assertEqual(myfunc('123 !'), '123 !')

	def test_type_error(self):
		with self.assertRaises(TypeError):
			myfunc(1)

if __name__ == '__main__':
	unittest.main()