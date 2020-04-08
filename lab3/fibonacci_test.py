import unittest
from fibonacci import fibonacci


class FibonacciTest(unittest.TestCase):
	def test_fibonacci_1(self):
		self.assertEqual(fibonacci(1), 1)

	def test_fibonacci_negative_number(self):
		self.assertEqual(fibonacci(-5), 0)

	def test_fibonacci_zero(self):
		self.assertEqual(fibonacci(0), 0)

	def test_fibonacci_positive_number_2(self):
		self.assertEqual(fibonacci(2), 1)

	def test_fibonacci_positive_number_3(self):
		self.assertEqual(fibonacci(6), 8)

	def test_fibonacci_positive_number_4(self):
		self.assertEqual(fibonacci(10), 55)


if __name__ == '__main__':
	unittest.main()
