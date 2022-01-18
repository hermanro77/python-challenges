class TicTacToe:
	def __init__(self):
		self.board = []
		for c in range(9):
			self.board.append(' ')

		self.player = 'X'

	def checkWin(self):
		win = False

		def check3(a, b, c):
			nonlocal win # access from parent function
			if self.board[a] == self.board[b] == self.board[c] == self.player:
				win = True

		for i in range(3):
			# Check horizontal
			check3(i * 3, (i * 3) + 1, (i * 3) + 2)
			# Check vertical
			check3(i, i + 3, i + 6)

		# Check top left diagonal
		check3(0, 4, 8)
		# Check bottom left diagonal
		check3(2, 4, 6)

		return win
	
	def checkTie(self):
		for c in self.board:
			if c == ' ':
				return False
		return True

	def nextPlayer(self):
		self.player = 'X' if self.player == 'O' else 'O'

	def printBoard(self):
		print('┌───┬───┬───┐')
		for r in range(3):
			r = (2 - r) * 3
			print(f'│ {self.board[r]} │ {self.board[r + 1]} │ {self.board[r + 2]} │')
			if r != 0:
				print('├───┼───┼───┤')
		print('└───┴───┴───┘')

	def start(self):
		self.printBoard()
		while True:
			print(f'Player {self.player}\'s turn')

			try:
				choice = int(input('Enter box number: ')) - 1
				if (choice < 0) or (choice >= 9):
					raise ValueError
			except ValueError:
				print('Please enter a number from 1-9')
				continue

			if self.board[choice] != ' ':
				print('That spot has already been taken')
				continue
			
			self.board[choice] = self.player
			self.printBoard()

			if self.checkWin():
				print(f'Player {self.player} won!')
			elif self.checkTie():
				print('It\'s a tie!')
			else:
				self.nextPlayer()
				continue

			if str(input('Play again? '))[:1] == 'y':
				self.__init__()
				self.start()
			else:
				break

# Sample usage:
# game = TicTacToe()
# game.start()

# Testing
import unittest
from unittest.mock import patch
from io import StringIO

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
