# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(nums):
	mysum = 0
	flag = False

	for num in nums:
		if num == 6:
			flag = True
		elif flag and num == 9: # only the next 9 after the 6
			flag = False
		elif not flag:
			mysum += num

	return mysum

# Testing
import unittest

class Test(unittest.TestCase):
	def test_normal(self):
		self.assertEqual(summer_69([1, 3, 5]), 9)

	def test_gap(self):
		self.assertEqual(summer_69([4, 5, 6, 7, 8, 9]), 9)

	def test_empty_gap(self):
		self.assertEqual(summer_69([2, 1, 6, 9, 11]), 14)

	def test_two_nines(self):
		self.assertEqual(summer_69([2, 1, 6, 9, 9, 11]), 23)

	def test_empty(self):
		self.assertEqual(summer_69([6, 1, 9]), 0)

	def test_empty_input(self):
		self.assertEqual(summer_69([]), 0)

if __name__ == '__main__':
	unittest.main()