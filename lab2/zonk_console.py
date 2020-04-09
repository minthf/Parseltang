from tkinter import *
from math import *
import random
from zonk_points import calc_zonk_combo

dice_length = 40


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Circle:
	def __init__(self, first: Point, second: Point):
		self.first_point = first
		self.second_point = second

	def draw_circle(self):
		place_dice.create_oval((self.first_point.x + self.second_point.x) / 2,
		                       (self.first_point.y + self.second_point.y) / 2,
		                       (self.first_point.x + self.second_point.x) / 2,
		                       (self.first_point.y + self.second_point.y) / 2, width=5)


def circle(first: Point, second: Point, third: Point, fourth: Point, center: Point, dice: list):
	circle_quantity = random.randint(1, 6)
	dice.append(circle_quantity)
	if (circle_quantity == 1 or circle_quantity == 5 or circle_quantity == 3):
		first_circle = Circle(center, center)
		first_circle.draw_circle()
	if (
			circle_quantity == 2 or circle_quantity == 3 or circle_quantity == 4 or circle_quantity == 5 or circle_quantity == 6):
		second_circle = Circle(center, first)
		second_circle.draw_circle()

		third_circle = Circle(center, third)
		third_circle.draw_circle()
	if (circle_quantity == 4 or circle_quantity == 6 or circle_quantity == 5):
		fourt_circle = Circle(center, fourth)
		fourt_circle.draw_circle()

		fifth_circle = Circle(center, second)
		fifth_circle.draw_circle()
	if (circle_quantity == 6):
		point_for_sixth_circle = Point((first.x + fourth.x) / 2, (first.y + fourth.y) / 2)
		point_for_seveth_circle = Point((second.x + third.x) / 2, (second.y + third.y) / 2)
		sixth_circle = Circle(center, point_for_sixth_circle)
		sixth_circle.draw_circle()

		seventh_circle = Circle(center, point_for_seveth_circle)
		seventh_circle.draw_circle()


def from_degrees_to_radians(degree):
	radian = degree * (pi / 180)
	return radian


def find_point(start: Point, angle, dice_length):
	x = start.x + (cos(angle) * dice_length)
	y = start.y - (sin(angle) * dice_length)
	return Point(x, y)


def create_dice():
	place_dice.delete("all")
	dice = []
	for i in range(random.randint(1, 6)):
		x = random.randint(50, 350)
		y = random.randint(50, 150)
		first_point = Point(x, y)
		angle = from_degrees_to_radians(random.randint(1, 360))
		x2 = first_point.x + (cos(angle) * dice_length)
		y2 = first_point.y - (sin(angle) * dice_length)
		second_point = Point(x2, y2)
		x4 = first_point.x + (sin(angle) * dice_length)
		y4 = first_point.y + (cos(from_degrees_to_radians(360) - angle) * dice_length)
		fourth_point = Point(x4, y4)
		ox = (second_point.x + fourth_point.x) / 2
		oy = (second_point.y + fourth_point.y) / 2
		center_point = Point(ox, oy)
		x3 = 2 * center_point.x - first_point.x
		y3 = 2 * center_point.y - first_point.y
		third_point = Point(x3, y3)
		place_dice.create_polygon(first_point.x, first_point.y, second_point.x, second_point.y, third_point.x,
		                          third_point.y, fourth_point.x, fourth_point.y, fill='white')
		circle(first_point, second_point, third_point, fourth_point, center_point, dice)
	points = calc_zonk_combo(dice)
	label_points = Label(text=points, font="Arial 14")
	label_points.place(x=200, y=250)


def quit():
	exit()


root = Tk()
root.geometry('500x360')
root.title("Zonk")
place_dice = Canvas(root, width=400, height=200, bg='green')
place_dice.place(x=10, y=10)

button_play = Button(root, text="roll the dice", command=create_dice)
button_quit = Button(root, text="Quit", command=quit)

button_play.place(x=100, y=300)
button_quit.place(x=300, y=300)
root.mainloop()
