def list_of_numbers(a, b):
	if a < b:
		return [a] + list_of_numbers(a+1, b)
	else:
		return []