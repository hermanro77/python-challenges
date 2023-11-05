# Testing
import unittest
from challenges.expert.blackjack import blackjack

class Test(unittest.TestCase):
	def test_normal(self):
		self.assertEqual(blackjack(5, 6, 7), 18)

	def test_ace(self):
		self.assertEqual(blackjack(9, 9, 11), 19)

	def test_bust(self):
		self.assertEqual(blackjack(9, 9, 9), 'BUST')

if __name__ == '__main__':
	unittest.main()