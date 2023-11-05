# Testing
import unittest
from unittest.mock import patch
from io import StringIO
from challenges.expert.tic_tac_toe_oop import TicTacToe

class Test(unittest.TestCase):
	@patch('sys.stdout', new_callable=StringIO)
	def test_play_win(self, fake_print):
		i = 0
		def getNumber(_):
			nonlocal i
			i += 1
			return str(i)

		with patch('builtins.input', getNumber):
			game = TicTacToe()
			game.start()

			self.assertTrue(fake_print.getvalue().strip().split('\n')[-1].startswith('Player X won!'))

	@patch('sys.stdout', new_callable=StringIO)
	def test_play_tie(self, fake_print):
		inputs = [1, 2, 5, 3, 6, 4, 7, 9, 8, 'n']
		def getInput(_):
			return str(inputs.pop(0))

		with patch('builtins.input', getInput):
			game = TicTacToe()
			game.start()

			self.assertTrue(fake_print.getvalue().strip().split('\n')[-1].startswith('It\'s a tie!'))

	def test_logic_win(self):
		game = TicTacToe()

		game.board = [
			'X', 'X', ' ',
			'O', 'X', 'O',
			' ', 'X', 'O'
		]

		self.assertTrue(game.checkWin())
		self.assertFalse(game.checkTie())

	def test_logic_tie(self):
		game = TicTacToe()

		game.board = [
			'X', 'O', 'O',
			'O', 'X', 'X',
			'X', 'X', 'O'
		]

		self.assertFalse(game.checkWin())
		self.assertTrue(game.checkTie())

if __name__ == '__main__':
	unittest.main()
