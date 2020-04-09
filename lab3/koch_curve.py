from PIL import Image, ImageColor
from PIL import ImageDraw
import math as m

image = Image.new("RGB", (400, 300))
draw = ImageDraw.Draw(image)


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def find_part_of_line(start: Point, end: Point, part):
	y = (start.y + (part * end.y)) / (1 + part)
	x = (start.x + (part * end.x)) / (1 + part)
	return Point(x, y)


def draw_koh_curve(start: Point, end: Point, deep=3):
	if deep == 1:
		return
	length = m.sqrt(pow((start.x - end.x), 2) + pow((start.y - end.y), 2))

	second_point = find_part_of_line(start, end, 1 / 2)
	fourth_point = find_part_of_line(start, end, 2)

	angle = m.atan((start.y - end.y) / (end.x - start.x))
	if end.x < start.x:
		angle += m.pi

	triangle_angle = (m.pi / 3) + angle
	cx = second_point.x + (m.cos(triangle_angle) * (length / 3))
	cy = second_point.y - (m.sin(triangle_angle) * (length / 3))
	third_point = Point(cx, cy)

	draw.line((second_point.x, second_point.y, third_point.x, third_point.y))
	draw.line((third_point.x, third_point.y, fourth_point.x, fourth_point.y))
	draw.line((second_point.x, second_point.y, fourth_point.x, fourth_point.y), fill=ImageColor.getrgb("black"))

	draw_koh_curve(start, second_point, deep - 1)
	draw_koh_curve(second_point, third_point, deep - 1)
	draw_koh_curve(third_point, fourth_point, deep - 1)
	draw_koh_curve(fourth_point, end, deep - 1)


start_point = Point(10, 200)
end_point = Point(390, 200)
draw.line((start_point.x, start_point.y, end_point.x, end_point.y))

draw_koh_curve(start_point, end_point, 5)
image.save("picture_koch.png", "PNG")
image.show()
