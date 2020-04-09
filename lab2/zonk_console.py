from tkinter import *
from math import *
import random
from zonk_points import calc_zonk_combo

DICE_LENGTH = 40


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Dice:
	def __init__(self, first: Point, second: Point, third: Point, fourth: Point):
		self.first_point = first
		self.second_point = second
		self.third_point = third
		self.fourth_point = fourth

	def draw_dice(self):
		place_dice.create_polygon(
			self.first_point.x, self.first_point.y, self.second_point.x, self.second_point.y,
		    self.third_point.x, self.third_point.y, self.fourth_point.x, self.fourth_point.y, fill='white'
		)


class Circle:
	def __init__(self, first: Point, second: Point):
		self.first_point = first
		self.second_point = second

	def draw_circle(self):
		place_dice.create_oval(
			(self.first_point.x + self.second_point.x) / 2,
			(self.first_point.y + self.second_point.y) / 2,
			(self.first_point.x + self.second_point.x) / 2,
			(self.first_point.y + self.second_point.y) / 2, width=5)


def quantity_of_circles(first: Point, second: Point, third: Point, fourth: Point, center: Point, dice_points: list):
	circle_quantity = random.randint(1, 6)
	dice_points.append(circle_quantity)
	if circle_quantity in [1, 5, 3]:
		first_circle = Circle(center, center)
		first_circle.draw_circle()
	if circle_quantity in [2, 3, 4, 5, 6]:
		second_circle = Circle(center, first)
		second_circle.draw_circle()

		third_circle = Circle(center, third)
		third_circle.draw_circle()
	if circle_quantity in [4, 5, 6]:
		fourt_circle = Circle(center, fourth)
		fourt_circle.draw_circle()

		fifth_circle = Circle(center, second)
		fifth_circle.draw_circle()
	if circle_quantity == 6:
		point_for_sixth_circle = Point((first.x + fourth.x) / 2, (first.y + fourth.y) / 2)
		point_for_seveth_circle = Point((second.x + third.x) / 2, (second.y + third.y) / 2)

		sixth_circle = Circle(center, point_for_sixth_circle)
		sixth_circle.draw_circle()

		seventh_circle = Circle(center, point_for_seveth_circle)
		seventh_circle.draw_circle()


def from_degrees_to_radians(degree):
	radian = degree * (pi / 180)
	return radian


def create_dice():
	place_dice.delete("all")
	dice_points = []
	for i in range(random.randint(1, 6)):
		x = random.randint(50, 350)
		y = random.randint(50, 150)
		first_point = Point(x, y)
		angle = from_degrees_to_radians(random.randint(1, 360))
		x2 = first_point.x + (cos(angle) * DICE_LENGTH)
		y2 = first_point.y - (sin(angle) * DICE_LENGTH)
		second_point = Point(x2, y2)
		x4 = first_point.x + (sin(angle) * DICE_LENGTH)
		y4 = first_point.y + (cos(from_degrees_to_radians(360) - angle) * DICE_LENGTH)
		fourth_point = Point(x4, y4)
		ox = (second_point.x + fourth_point.x) / 2
		oy = (second_point.y + fourth_point.y) / 2
		center_point = Point(ox, oy)
		x3 = 2 * center_point.x - first_point.x
		y3 = 2 * center_point.y - first_point.y
		third_point = Point(x3, y3)
		dice = Dice(first_point, second_point, third_point, fourth_point)
		dice.draw_dice()
		quantity_of_circles(first_point, second_point, third_point, fourth_point, center_point, dice_points)
	points = calc_zonk_combo(dice_points)
	label_points = Label(text=points, font="Arial 14")
	label_points.place(x=200, y=250)


def exit_program():
	exit()

root = Tk()
root.geometry('500x360')
root.title("Zonk")
place_dice = Canvas(root, width=400, height=200, bg='green')
place_dice.place(x=10, y=10)

button_play = Button(root, text="roll the dice", command=create_dice)
button_quit = Button(root, text="Quit", command=exit_program)

button_play.place(x=100, y=300)
button_quit.place(x=300, y=300)
root.mainloop()
