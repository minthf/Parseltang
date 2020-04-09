import math
from PIL import Image, ImageDraw, ImageColor


class Point:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y


class Line:
	def __init__(self, first: Point, second: Point):
		self.first_point = first
		self.second_point = second

	def draw_line(self, color):
		draw.line((self.first_point.x, self.first_point.y, self.second_point.x, self.second_point.y),
		          fill=ImageColor.getrgb(color))


def distance(start: Point, end: Point):
	dx = start.x - end.x
	dy = start.y - end.y
	return math.sqrt(dx ** 2 + dy ** 2)


def point_by_angle(line_angle, angle, turn_angle, point: Point, length):
	point_angle = line_angle + turn_angle + angle
	x = point.x + math.cos(point_angle) * length
	y = point.y - math.sin(point_angle) * length
	return Point(x, y)


def draw_fern(start: Point, end: Point, deep=2, angle=0.1524):
	length = distance(start, end)
	if deep == 1:
		return

	if (end.x - start.x) == 0:
		line_angle = math.atan((start.y - end.y))
	else:
		line_angle = math.atan((start.y - end.y) / (end.x - start.x))
		if end.x < start.x:
			line_angle += math.pi

	third_x = start.x + 2 * (end.x - start.x) / 4
	third_y = start.y + 2 * (end.y - start.y) / 4
	third_point = Point(third_x, third_y)

	fourth_point = point_by_angle(line_angle, angle, math.pi / 4, third_point, length / 2)
	first_line = Line(third_point,fourth_point)
	first_line.draw_line("red")
	draw_fern(third_point, fourth_point, deep - 1)

	x6 = start.x + 2 * (end.x - start.x) / 6
	y6 = start.y + 2 * (end.y - start.y) / 6
	sixth_point = Point(x6, y6)

	fifth_point = point_by_angle(line_angle, angle, -math.pi / 4, sixth_point, length / 2)
	second_line = Line(sixth_point,fifth_point)
	second_line.draw_line("green")
	draw_fern(sixth_point, fifth_point, deep - 1)

	next_point = point_by_angle(line_angle, angle, -math.pi / 12, end, length / 1.5)
	third_line = Line(end,next_point)
	third_line.draw_line("yellow")
	draw.line((end.x, end.y, next_point.x, next_point.y), fill=ImageColor.getrgb("green"))
	draw_fern(end, next_point, deep - 1)


width, height = 1200, 680

image = Image.new("RGB", (width, height))
draw = ImageDraw.ImageDraw(image)

start_point = Point(200, 600)
end_point = Point(400, 400)
draw.line((start_point.x, start_point.y, end_point.x, end_point.y))
draw_fern(start_point, end_point, 10)

image.save("BransleyFern.png")
image.show()
