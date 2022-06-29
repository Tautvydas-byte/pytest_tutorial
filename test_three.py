import unittest
# default unittest template if create new py file choose for unit test

class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
	unittest.main()
