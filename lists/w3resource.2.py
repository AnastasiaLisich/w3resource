array = [20, 45, -777, -1980, 690, 4, 55]

min = None

for current in array:
    if min is None:
        min = current
    elif current < min:
        min = current

print(min)	
