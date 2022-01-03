import random

# this would probably be wrapped in a while loop instead of a function
def game():
	num = random.randint(1, 100)
	guess = 0
	tries = 1

	while guess != num:
		try:
			guess = int(input('Guess a number between 1 and 100: '))
			print(guess)
			if guess > num:
				print('Too high!')
			elif guess < num:
				print('Too low!')
			else:
				print(f'You got it after {tries} tries. It was {num}.')
				break
			tries += 1
		except ValueError:
			print('That\'s not a number')

# Testing
import unittest
from unittest.mock import patch
from io import StringIO

class Test(unittest.TestCase):
	# work alternating between up down from 100 and up from 0 (100, 1, 99, 2, ...)
	# this should cover both "Too high!" and "Too low!"
	i = 0
	flag = True
	def getNumber(self, _):
		if self.flag:
			guess = 100 - self.i
			self.i += 1
		else:
			guess = self.i
		self.flag = not self.flag
		return guess

	@patch('sys.stdout', new_callable=StringIO)
	def test(self, fake_print):
		with patch('builtins.input', self.getNumber):
			game()

			self.assertTrue(fake_print.getvalue().strip().split("\n")[-1].startswith('You got it'))

if __name__ == '__main__':
	unittest.main()