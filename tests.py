import unittest
from stocks_tests_version import Stock
import pandas

class stocksTest(unittest.TestCase):
	def setup(self):
		#self.stock = pandas.read_csv('test_data.csv')
		self.stock = Stock('FB', 'QG4NNRJQYXX2Q37D', 'pK79hjJb6QJSsgQPtHbX')
	


if __name__ == '__main__':
	unittest.main()