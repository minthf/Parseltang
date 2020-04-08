def max_in_list(list):
	if len(list) == 0:
		return []
	if len(list) == 1:
		return list[0]
	elif list[0] > list[1]:
		return max_in_list(list[:1] + list[2:])
	else:
		return max_in_list(list[1:])