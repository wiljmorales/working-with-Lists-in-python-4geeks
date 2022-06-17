all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(color_list):
	return list(filter(lambda element: element["sexy"], color_list))

def generate_li(color_dict):
	return "<li>" + color_dict["label"] + "</li>"

print(list(map(generate_li, filter_colors(all_colors))))
