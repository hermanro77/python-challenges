# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):
	mysum = sum([a, b, c])

	if mysum <= 21:
		return mysum
	elif 11 in (a, b, c) and mysum - 10 <= 21:
		return mysum - 10
	else:
		return 'BUST'

# Testing
import unittest

class Test(unittest.TestCase):
	def test_normal(self):
		self.assertEqual(blackjack(5, 6, 7), 18)

	def test_ace(self):
		self.assertEqual(blackjack(9, 9, 11), 19)

	def test_bust(self):
		self.assertEqual(blackjack(9, 9, 9), 'BUST')

if __name__ == '__main__':
	unittest.main()