WIDTH = 1000

#barn is a list of 0s that is 1000 by 1000
barn = [[0 for _ in range(WIDTH + 1)] for _ in range(WIDTH + 1)]

#read in data from input file and assign the two values in the first line to rectangles and paint
with open("paintbarn.in") as read:
	rectangles, paint = [int(i) for i in read.readline().split()]

	#for rectangles number of times we get the x and y values for the rectangles from input file
	for _ in range(rectangles):
		start_x, start_y, end_x, end_y = [int(i) for i in read.readline().split()]
		# we can add and subtract 1 from the barn array using the values of the coners of the rectangles
		barn[start_x][start_y] += 1
		barn[start_x][end_y] -= 1
		barn[end_x][start_y] -= 1
		barn[end_x][end_y] += 1

area = 0

# Run 2D prefix sums on the array
for x in range(WIDTH + 1):
	for y in range(WIDTH + 1):
		if x > 0:
			barn[x][y] += barn[x - 1][y]
		if y > 0:
			barn[x][y] += barn[x][y - 1]
		if x > 0 and y > 0:
			barn[x][y] -= barn[x - 1][y - 1]
		area += barn[x][y] == paint

print(area, file=open("paintbarn.out", "w"))