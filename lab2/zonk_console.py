from tkinter import *
from math import *
import random

dice_length = 40


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def circle(first: Point, second: Point, third: Point, fourth: Point, center: Point):
	circle_quantity = random.randint(1, 6)
	if (circle_quantity == 1):
		place_dice.create_oval(center.x, center.y, center.x + 1, center.y + 1, width=5)
	elif (circle_quantity == 2):
		place_dice.create_oval((center.x + first.x) / 2, (center.y + first.y) / 2, (center.x + first.x) / 2, (center.y + first.y) / 2, width=5)
		place_dice.create_oval((center.x + third.x) / 2, (center.y + third.y) / 2, (center.x + third.x) / 2, (center.y + third.y) / 2, width=5)
	elif (circle_quantity == 3):
		place_dice.create_oval((center.x + first.x) / 2, (center.y + first.y) / 2, (center.x + first.x) / 2, (center.y + first.y) / 2, width=5)
		place_dice.create_oval((center.x + third.x) / 2, (center.y + third.y) / 2, (center.x + third.x) / 2, (center.y + third.y) / 2, width=5)
		place_dice.create_oval(center.x, center.y, center.x + 1, center.y + 1, width=5)
	elif (circle_quantity == 4):
		place_dice.create_oval((center.x + first.x) / 2, (center.y + first.y) / 2, (center.x + first.x) / 2, (center.y + first.y) / 2, width=5)
		place_dice.create_oval((center.x + third.x) / 2, (center.y + third.y) / 2, (center.x + third.x) / 2, (center.y + third.y) / 2, width=5)
		place_dice.create_oval((center.x + fourth.x) / 2, (center.y + fourth.y) / 2, (center.x + fourth.x) / 2, (center.y + fourth.y) / 2, width=5)
		place_dice.create_oval((center.x + second.x) / 2, (center.y + second.y) / 2, (center.x + second.x) / 2, (center.y + second.y) / 2, width=5)
	elif (circle_quantity == 5):
		place_dice.create_oval((center.x + first.x) / 2, (center.y + first.y) / 2, (center.x + first.x) / 2, (center.y + first.y) / 2, width=5)
		place_dice.create_oval((center.x + third.x) / 2, (center.y + third.y) / 2, (center.x + third.x) / 2, (center.y + third.y) / 2, width=5)
		place_dice.create_oval((center.x + fourth.x) / 2, (center.y + fourth.y) / 2, (center.x + fourth.x) / 2, (center.y + fourth.y) / 2, width=5)
		place_dice.create_oval((center.x + second.x) / 2, (center.y + second.y) / 2, (center.x + second.x) / 2, (center.y + second.y) / 2, width=5)
		place_dice.create_oval(center.x, center.y, center.x + 1, center.y + 1, width=5)
	elif (circle_quantity == 6):
		place_dice.create_oval((center.x + first.x) / 2, (center.y + first.y) / 2, (center.x + first.x) / 2, (center.y + first.y) / 2, width=5)
		place_dice.create_oval((center.x + third.x) / 2, (center.y + third.y) / 2, (center.x + third.x) / 2, (center.y + third.y) / 2, width=5)
		place_dice.create_oval((center.x + fourth.x) / 2, (center.y + fourth.y) / 2, (center.x + fourth.x) / 2, (center.y + fourth.y) / 2, width=5)
		place_dice.create_oval((center.x + second.x) / 2, (center.y + second.y) / 2, (center.x + second.x) / 2, (center.y + second.y) / 2, width=5)
		place_dice.create_oval((center.x + ((first.x + fourth.x) / 2)) / 2, (center.y + ((first.y + fourth.y) / 2)) / 2, (center.x + ((first.x + fourth.x) / 2)) / 2,
		                       (center.y + ((first.y + fourth.y) / 2)) / 2, width=5)
		place_dice.create_oval((center.x + ((second.x + third.x) / 2)) / 2, (center.y + ((second.y + third.y) / 2)) / 2, (center.x + ((second.x + third.x) / 2)) / 2,
		                       (center.y + ((second.y + third.y) / 2)) / 2, width=5)


def create_dice():
	place_dice.delete("all")
	for i in range(random.randint(1, 6)):
		x = random.randint(50, 350)
		y = random.randint(50, 150)
		first_point = Point(x, y)
		angle = random.randint(1, 360) * (3.1415926 / 180)
		x2 = x + (cos(angle) * dice_length)
		y2 = y - (sin(angle) * dice_length)
		second_point = Point(x2, y2)
		x4 = x + (sin(angle) * dice_length)
		y4 = y + (cos((360 * (3.1415926 / 180)) - angle) * dice_length)
		fourth_point = Point(x4, y4)
		ox = (x2 + x4) / 2
		oy = (y2 + y4) / 2
		center_point = Point(ox, oy)
		x3 = 2 * ox - x
		y3 = 2 * oy - y
		third_point = Point(x3, y3)
		place_dice.create_polygon(first_point.x, first_point.y, second_point.x, second_point.y, third_point.x,
		                          third_point.y, fourth_point.x, fourth_point.y, fill='white')
		circle(first_point, second_point, third_point, fourth_point, center_point)


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
