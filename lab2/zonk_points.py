class Zonk_calculator:
	def set_of_three_or_more(self,dice):  # функция проверяет комбинации: три одинаковых, четвертая/пятая/шестая кость
		temp_sum = 0
		points = {  # хранятся очки для комбинаций
			1: 1000,
			2: 200,
			3: 300,
			4: 400,
			5: 500,
			6: 600
		}
		for point, score in points.items():
			if dice.count(point) >= 3:
				multiplier = dice.count(point) - 2
				temp_sum += score * multiplier
				if point == 1 or point == 5:
					global run_ones_fives
					run_ones_fives = False
		return temp_sum


	def ones_and_fives(self,dice, dice_sum):
		for element in dice:
			if element == 1:
				dice_sum = dice_sum + 100
			if element == 5:
				dice_sum = dice_sum + 50
		return dice_sum


	def all_different(self,dice):
		if dice == [1, 2, 3, 4, 5, 6]:
			return True


	def three_couple(self, dice):
		count = 0
		for i in range(1, 7):
			if dice.count(i) == 2:
				count += 1
		if count == 3:
			return True


	def calc_zonk_combo(self,dice):
		global run_ones_fives  # переменная проверяет были ли пары из 3х
		run_ones_fives = True
		dice.sort()
		dice_sum = 0
		if self.all_different(dice):
			return 1500
		if self.three_couple(dice):
			return 750
		sum_of_set_of_three = self.set_of_three_or_more(dice)
		dice_sum += sum_of_set_of_three
		if run_ones_fives:
			dice_sum =self.ones_and_fives(dice, dice_sum)
		return dice_sum


calculator = Zonk_calculator()


def set_of_three_or_more(dice):  # функция проверяет комбинации: три одинаковых, четвертая/пятая/шестая кость
	temp_sum = 0
	points = {  # хранятся очки для комбинаций
		1: 1000,
		2: 200,
		3: 300,
		4: 400,
		5: 500,
		6: 600
	}
	for point, score in points.items():
		if dice.count(point) >= 3:
			multiplier = dice.count(point) - 2
			temp_sum += score * multiplier
			if point == 1 or point == 5:
				global run_ones_fives
				run_ones_fives = False
	return temp_sum


def ones_and_fives(dice, dice_sum):
	for element in dice:
		if element == 1:
			dice_sum = dice_sum + 100
		if element == 5:
			dice_sum = dice_sum + 50
	return dice_sum


def all_different(dice):
	if dice == [1, 2, 3, 4, 5, 6]:
		return True


def three_couple(dice):
	count = 0
	for i in range(1, 7):
		if dice.count(i) == 2:
			count += 1
	if count == 3:
		return True


def calc_zonk_combo(dice):
	global run_ones_fives  # переменная проверяет были ли пары из 3х
	run_ones_fives = True
	dice.sort()
	dice_sum = 0
	if all_different(dice):
		return 1500
	if three_couple(dice):
		return 750
	sum_of_set_of_three = set_of_three_or_more(dice)
	dice_sum += sum_of_set_of_three
	if run_ones_fives:
		dice_sum = ones_and_fives(dice, dice_sum)
	return dice_sum


