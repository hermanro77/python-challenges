# Given a string, return a string where for every character in the original there are 3 originals.

def paper_doll(text):
	result = ''

	for char in text:
		result += char * 3

	return result

# Testing
import unittest

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(paper_doll('Hello'), 'HHHeeellllllooo')

	def test_2(self):
		self.assertEqual(paper_doll('Mississippi'), 'MMMiiissssssiiissssssiiippppppiii')

if __name__ == '__main__':
	unittest.main()