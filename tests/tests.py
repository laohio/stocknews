import unittest
from stocks import Stock
import pandas

class stocksTest(unittest.TestCase):
	def setup(self):
		self.stock = Stock('FB')
if __name__ == '__main__':
	unittest.main()