import math
from PIL import Image, ImageDraw, ImageColor


class Point:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y


def distance(start: Point, end: Point):
	dx = start.x - end.x
	dy = start.y - end.y
	return math.sqrt(dx ** 2 + dy ** 2)


class Dragon_curve:
	def __init__(self, start: Point, end: Point):
		self.start = start
		self.end = end

	def draw_dragon_curve(self, start: Point, end: Point, draw: ImageDraw.ImageDraw):
		length = distance(start, end)
		if length < 1:
			draw.line((int(round(start.x)), int(round(start.y)), int(round(end.x)), int(round(end.y))),
			          fill=ImageColor.getrgb("red"))
		else:
			if (end.x - start.x) == 0:
				line_angle = math.atan((start.y - end.y))
			else:
				line_angle = math.atan((start.y - end.y) / (end.x - start.x))
				if end.x < start.x:
					line_angle += math.pi

			point3_angle = line_angle + math.pi / 4
			point3_x = start.x + math.cos(point3_angle) * length / math.sqrt(2)
			point3_y = start.y - math.sin(point3_angle) * length / math.sqrt(2)
			point3 = Point(point3_x, point3_y)

			self.draw_dragon_curve(start, point3, draw)
			self.draw_dragon_curve(end, point3, draw)


width, height = 1200, 400

image = Image.new("RGB", (width, height))
draw = ImageDraw.ImageDraw(image)

start_point = Point(400, height - 200)
end_point = Point(700, height - 200)
dragon = Dragon_curve(start_point, end_point)
dragon.draw_dragon_curve(dragon.start, dragon.end, draw)

image.save("dragon_curve.png")
image.show()
