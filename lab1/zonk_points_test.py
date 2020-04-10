import unittest
from zonk_points import calculator

class TestZonkPoints(unittest.TestCase):
	def test_zonk_points_ones_and_fives(self):
		self.assertEqual(calculator.calc_zonk_combo([1, 1, 5, 5, 2, 3]), 300)

	def test_zonk_points_ones_and_fives_2(self):
		self.assertEqual(calculator.calc_zonk_combo([1, 1, 3, 5, 2, 3]), 250)

	def test_zonk_points_set_of_three(self):
		self.assertEqual(calculator.calc_zonk_combo([2, 2, 2, 4, 6, 3]), 200)

	def test_zonk_points_ones_and_fives_and_set_of_three(self):
		self.assertEqual(calculator.calc_zonk_combo([2, 2, 2, 1, 5, 3]), 350)

	def test_zonk_points_set_of_four(self):
		self.assertEqual(calculator.calc_zonk_combo([2, 2, 2, 2, 4, 3]), 400)

	def test_zonk_points_set_of_five(self):
		self.assertEqual(calculator.calc_zonk_combo([3, 3, 3, 3, 4, 3]), 900)

	def test_zonk_points_set_of_six(self):
		self.assertEqual(calculator.calc_zonk_combo([6, 6, 6, 6, 6, 6]), 2400)

	def test_zonk_points_double_set_of_three(self):
		self.assertEqual(calculator.calc_zonk_combo([6, 6, 6, 3, 3, 3]), 900)

	def test_zonk_points_set_of_three_and_ones(self):
		self.assertEqual(calculator.calc_zonk_combo([6, 6, 6, 1, 1, 7]), 800)

	def test_zonk_points_set_of_six_2(self):
		self.assertEqual(calculator.calc_zonk_combo([1, 1, 1, 1, 1, 1]), 4000)

	def test_zonk_points_six_different(self):
		self.assertEqual(calculator.calc_zonk_combo([1, 2, 3, 4, 5, 6]), 1500)

	def test_zonk_points_three_couple(self):
		self.assertEqual(calculator.calc_zonk_combo([1, 1, 2, 2, 3, 3]), 750)

	def test_zonk_points_all_different(self):
		self.assertEqual(calculator.calc_zonk_combo([2, 4, 5, 3, 1, 6]), 1500)

	def test_zonk_points_fourth_fives_sixth_dice(self):
		self.assertEqual(calculator.calc_zonk_combo([6, 6, 6, 6, 6, 6]), 2400)

	def test_zonk_points_one_couple(self):
		self.assertEqual(calculator.calc_zonk_combo([1, 1, 1]), 1000)

	def test_zonk_points_four_same_and_one_couple(self):
		self.assertEqual(calculator.calc_zonk_combo([1, 1, 1, 1, 2, 2]), 2000)

	def test_zonk_points_one(self):
		self.assertEqual(calculator.calc_zonk_combo([1]), 100)

	def test_zonk_points_five(self):
		self.assertEqual(calculator.calc_zonk_combo([5]), 50)

	def test_zonk_points_no_combo(self):
		self.assertEqual(calculator.calc_zonk_combo([3, 4, 6, 7]), 0)

	def test_zonk_points_empty_dice(self):
		self.assertEqual(calculator.calc_zonk_combo([]), 0)


if __name__ == '__main__':
	unittest.main()
