# Define a function called myfunc that takes in an arbitrary number of values and returns the sums of those arguments.

def myfunc(*nums):
	sum = 0
	for num in nums:
		sum += num
	return sum

# This way is kind of cheating
# def myfunc(*nums):
# 	return sum(nums)

# Testing
import unittest

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(myfunc(1, 2, 3, 4, 5), 15)

	def test_one(self):
		self.assertEqual(myfunc(1), 1)

	def test_varied(self):
		self.assertEqual(myfunc(23, 34, 12), 69)

	def test_type_error(self):
		with self.assertRaises(TypeError):
			myfunc('string')

if __name__ == '__main__':
	unittest.main()