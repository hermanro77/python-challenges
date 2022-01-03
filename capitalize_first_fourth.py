# Write a function that capitalizes the first and fourth letters of a name (such as macdonald)

def myfunc(name):
	mylist = list(name) # split each letter
	mylist[0] = mylist[0].upper() # indexes start at 0 instead of 1
	mylist[3] = mylist[3].upper()
	return ''.join(mylist) # turn the list back into a string

# Testing
import unittest

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(myfunc('macdonald'), 'MacDonald')

	# Is this the right behavior?
	def test_short(self):
		with self.assertRaises(IndexError):
			myfunc('mac')

if __name__ == '__main__':
	unittest.main()