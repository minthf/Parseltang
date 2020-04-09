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


def draw_dragon_curve(start: Point, end: Point, draw: ImageDraw.ImageDraw):
	length = distance(start, end)
	if length < 1:
		draw.line((int(round(start.x)), int(round(start.y)), int(round(end.x)), int(round(end.y))), fill=ImageColor.getrgb("red"))
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

		draw_dragon_curve(start, point3, draw)
		draw_dragon_curve(end, point3, draw)


width, height = 1200, 400

image = Image.new("RGB", (width, height))
draw = ImageDraw.ImageDraw(image)

start_point = Point(400, height - 200)
end_point = Point(700, height - 200)
draw_dragon_curve(start_point, end_point, draw)

image.save("dragon_curve.png")
image.show()
