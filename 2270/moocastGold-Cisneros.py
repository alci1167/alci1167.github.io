from typing import NamedTuple

#class that implements Disjoint Set Union
class DSU:
	#initialize DSU with a given size
	def __init__(self, size: int) -> None:
		#initialize the size of each disjoint set to 1
		self.sizes = [1 for _ in range(size)]
		#initialize parent of each element to be itself
		self.parents = [i for i in range(size)]

	#get top level parent of the given element in the disjoint set
	def get_top(self, n: int) -> int:
		#if the element is already the top-level parent, we return it
		if self.parents[n] == n:
			return n
		#otherwise recursively get the top-level parent of the current parent
		self.parents[n] = self.get_top(self.parents[n])
		#once the top level parent is found, we set it as the parent of the current element
		return self.parents[n]

	#link the disjoint sets of two given elements together
	def link(self, n1: int, n2: int) -> bool:
		#get top-level parents of the two elements
		n1 = self.get_top(n1)
		n2 = self.get_top(n2)
		#if two elements already belong to the same disjoint set, we return False
		if n1 == n2:
			return False

		#if the size of the disjoint set containing n1 is smaller than the size of the disjoint set containing n2, we swap n1 and n2
		if self.sizes[n1] < self.sizes[n2]:
			n1, n2 = n2, n1

		#merge the two disjoint sets together by setting the parent of n2 to n1 and updating the size of the new disjoint set
		self.sizes[n1] += self.sizes[n2]
		self.parents[n2] = n1
		#return true to show that a new edge has been added to MST
		return True

#define a named tuple to represent edges between points
class Edge(NamedTuple):
	a: int
	b: int
	dist: int

#read in the input
with open("moocast.in") as read:
	n = int(read.readline())
	x = []
	y = []
	for i in range(n):
		x_i, y_i = [int(i) for i in read.readline().split()]
		x.append(x_i)
		y.append(y_i)

#the distances between each pair of points and we store them as edges
edges = []
for i in range(n):
	for j in range(i + 1, n):
		dx = x[i] - x[j]
		dy = y[i] - y[j]
		#the squared euclidean distance between the two points
		edges.append(Edge(i, j, dx**2 + dy**2))
#sort edges by distance
edges.sort(key=lambda e: e.dist)

#initialize the distance of the last added edge to 0
last_dist = 0
#initialize the number of connected components to n
comp_num = n
#initialize DSU
dsu = DSU(n)
#iterate through the sorted edges and add each edge to the MST if it connects two disconnected components
for e in edges:
	if dsu.link(e.a, e.b):
		#update distance of the last edge
            last_dist = e.dist
            comp_num -= 1
            if comp_num == 1:
                break
	    
with open("moocast.out", "w") as output:
    print(last_dist, file=output)
