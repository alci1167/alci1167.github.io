from collections import deque

with open("perimeter.in") as r:
	t = r.readline  #read first line of input file
	n = int(t())    #convert first line to integer, which is the size of the square grid
	ice = []        #list to store the data
	visited = [[False] * n for _ in range(n)]  #2D list of size n x n to keep track of visited cells

	#go through each line of input and store it as a list of characters in the ice list
	for _ in range(n):
		ice.append(list(t()))

max_area = 0     #store the maximum area of a connected component
min_peri = float("inf")   #store the minimum perimeter of a connected component

#directions to move from a cell to its neighbors (up, down, left, right)
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#check if cell is out of bounds
def out(a, b, l):
	if a < 0 or b < 0 or a >= l or b >= l:
		return True
	return False

#function to compute the area and perimeter of a connected component starting from cell (x, y)
def area_and_perimeter(x, y):
	area, peri = 1, 0  #area and perimeter to 1 and 0 respectively, since we start from a single cell

	q = deque()   #deque for breadth-first search
	q.append((x, y))  #add the starting cell to deque
	visited[x][y] = True   #mark the starting cell as visited

	#while deque is not empty, continue breadth-first search
	while q:
		x, y = q.pop()  #pop (remove) the last cell added to deque

		#loop through each neighbor of the current cell
		for dx, dy in DIRECTIONS:
			nx, ny = x + dx, y + dy   #calc the coordinates of the neighbor

			#if the neighbor is out of bounds or is an empty cell, perimeter +1
			if out(nx, ny, n) or ice[nx][ny] == ".":
				peri += 1
			else:
				#if the neighbor has not been visited, we add it to deque and mark as visited
				if not visited[nx][ny]:
					area += 1
					q.appendleft((nx, ny))
					visited[nx][ny] = True

	return area, peri   #return the area and perimeter of the connected component

#loop through each cell in the grid
for i in range(n):
	for j in range(n):
		#if the cell is part of a new connected component, we compute its area and perimeter
		if ice[i][j] == "#" and not visited[i][j]:
			area, peri = area_and_perimeter(i, j)

			#if area is greater than current max area, update max area and min perimeter
			if area > max_area:
				max_area, min_peri = area, peri
			#if area is equal to current max area, update min perimeter if it is smaller
			elif area == max_area:
				if min_peri > peri:
					max_area, min_peri = area, peri

print(max_area, min_peri, file=open("perimeter.out", "w"))
