import unittest
from max_in_list import max_in_list

class MaxInListTest(unittest.TestCase):
	def test_max_in_list_positive_list(self):
		self.assertEqual(max_in_list([1, 2, 3, 4, 5]), 5)

	def test_max_in_list_negative_list(self):
		self.assertEqual(max_in_list([-1, -2, -3, -4, -5]), -1)

	def test_max_in_list_negative_list_2(self):
		self.assertEqual(max_in_list([-1, -1, -3, -4, -5]), -1)

	def test_max_in_list_same_numbers(self):
		self.assertEqual(max_in_list([-1, -1, -1, -1]), -1)

	def test_max_in_list_empty_list(self):
		self.assertEqual(max_in_list([]), [])


if __name__ == '__main__':
	unittest.main()
