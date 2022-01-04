# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
	for i in range(len(nums) - 1): # get the index, not the value; offset by 1 as the last one is checked by the previous
		if (nums[i] == 3) and (nums[i + 1] == 3):
			return True # it just has to happen once, the specific location doesn't matter
	return False

# Testing
import unittest

class Test(unittest.TestCase):
	def test_true(self):
		self.assertTrue(has_33([1, 3, 3]))

	def test_false(self):
		self.assertFalse(has_33([1, 3, 1, 3]))

	def test_false_2(self):
		self.assertFalse(has_33([3, 1, 3]))

	def test_false_none(self):
		self.assertFalse(has_33([1, 2, 4]))

if __name__ == '__main__':
	unittest.main()