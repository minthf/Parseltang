import unittest
from range_between_two_numbers import list_of_numbers

class ListOfNumbersTest(unittest.TestCase):
	def test_range_same_numbers(self):
		self.assertEqual(list_of_numbers(1, 1), [])

	def test_range_positive_numbers(self):
		self.assertEqual(list_of_numbers(1, 5), [1, 2, 3, 4])

	def test_range_positive_numbers_2(self):
		self.assertEqual(list_of_numbers(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])

	def test_range_positive_and_negative_numbers(self):
		self.assertEqual(list_of_numbers(-5, 3), [-5, -4, -3, -2, -1, 0, 1, 2])

	def test_range_first_bigger_then_second(self):
		self.assertEqual(list_of_numbers(10, 1), [])

if __name__ == '__main__':
	unittest.main()
