# Testing
import unittest
from challenges.beginner.paper_doll import paper_doll

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(paper_doll('Hello'), 'HHHeeellllllooo')

	def test_2(self):
		self.assertEqual(paper_doll('Mississippi'), 'MMMiiissssssiiissssssiiippppppiii')

if __name__ == '__main__':
	unittest.main()