from tkinter import *
from math import *
from random import randint
from zonk_points import calc_zonk_combo

DICE_LENGTH = 40


class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Dice:
	def __init__(self):
		x = randint(50, 350)
		y = randint(50, 150)
		self.first_point = Coordinate(x, y)
		angle = from_degrees_to_radians(randint(1, 360))
		x2 = self.first_point.x + (cos(angle) * DICE_LENGTH)
		y2 = self.first_point.y - (sin(angle) * DICE_LENGTH)
		self.second_point = Coordinate(x2, y2)
		x4 = self.first_point.x + (sin(angle) * DICE_LENGTH)
		y4 = self.first_point.y + (cos(from_degrees_to_radians(360) - angle) * DICE_LENGTH)
		self.fourth_point = Coordinate(x4, y4)
		ox = (self.second_point.x + self.fourth_point.x) / 2
		oy = (self.second_point.y + self.fourth_point.y) / 2
		self.center_point = Coordinate(ox, oy)
		x3 = 2 * self.center_point.x - self.first_point.x
		y3 = 2 * self.center_point.y - self.first_point.y
		self.third_point = Coordinate(x3, y3)

		self.roll()

	def roll(self):
		self.points = randint(1, 6)
		
	def get_points(self):
		return self.points
		
	def draw(self):
		place_dice.create_polygon(
			self.first_point.x, self.first_point.y, self.second_point.x, self.second_point.y,
		    self.third_point.x, self.third_point.y, self.fourth_point.x, self.fourth_point.y, fill='white'
		)
		circle_quantity = randint(1, 6)
		if circle_quantity in [1, 5, 3]:
			first_circle = Circle(self.center_point, self.center_point)
			first_circle.draw_circle()
		if circle_quantity in [2, 3, 4, 5, 6]:
			second_circle = Circle(self.center_point, self.first_point)
			second_circle.draw_circle()

			third_circle = Circle(self.center_point, self.third_point)
			third_circle.draw_circle()
		if circle_quantity in [4, 5, 6]:
			fourt_circle = Circle(self.center_point, self.fourth_point)
			fourt_circle.draw_circle()

			fifth_circle = Circle(self.center_point, self.second_point)
			fifth_circle.draw_circle()
		if circle_quantity == 6:
			point_for_sixth_circle = Coordinate((self.first_point.x + self.fourth_point.x) / 2, (self.first_point.y + self.fourth_point.y) / 2)
			point_for_seveth_circle = Coordinate((self.second_point.x + self.third_point.x) / 2, (self.second_point.y + self.third_point.y) / 2)

			sixth_circle = Circle(self.center_point, point_for_sixth_circle)
			sixth_circle.draw_circle()

			seventh_circle = Circle(self.center_point, point_for_seveth_circle)
			seventh_circle.draw_circle()


class Circle:
	def __init__(self, first: Coordinate, second: Coordinate):
		self.first_point = first
		self.second_point = second

	def draw_circle(self):
		place_dice.create_oval(
			(self.first_point.x + self.second_point.x) / 2,
			(self.first_point.y + self.second_point.y) / 2,
			(self.first_point.x + self.second_point.x) / 2,
			(self.first_point.y + self.second_point.y) / 2, width=5)




def from_degrees_to_radians(degree):
	radian = degree * (pi / 180)
	return radian


def create_dice():
	place_dice.delete("all")
	dices = []
	for i in range(randint(1, 6)):
		dices.append(Dice())
	points = []
	for dice in dices:
		dice.draw()
		points.append(dice.get_points())
	label_points["text"] = calc_zonk_combo(points)


def exit_program():
	exit()

root = Tk()
root.geometry('500x360')
root.title("Zonk")
place_dice = Canvas(root, width=400, height=200, bg='green')
place_dice.place(x=10, y=10)

label_points = Label(text="0000", font="Arial 14")
button_play = Button(root, text="roll the dice", command=create_dice)
button_quit = Button(root, text="Quit", command=exit_program)

label_points.place(x=200, y=250)
button_play.place(x=100, y=300)
button_quit.place(x=300, y=300)
root.mainloop()
