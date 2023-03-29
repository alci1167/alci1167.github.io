#open input and output files
fin, fout = open("billboard.in"), open("billboard.out", "w")

#read coordinates from input file
Mx1, My1, Mx2, My2 = map(int, fin.readline().split()) #lawn mower billboard
Fx1, Fy1, Fx2, Fy2 = map(int, fin.readline().split()) #cow feed billboard

#lists of x and y coordinates for indexing
xCoords = [0, Mx1, Mx2, Fx1, Fx2]
yCoords = [0, My1, My2, Fy1, Fy2]

#check if billboard is completely covered by mower billboard
if xCoords[4] >= xCoords[2] and xCoords[3] <= xCoords[1] and yCoords[4] >= yCoords[2] and yCoords[3] <= yCoords[1]:
	fout.write(str(0))
#check if mower billboard covers top part of billboard
elif xCoords[3] <= xCoords[1] and yCoords[3] <= yCoords[1] and yCoords[4] > yCoords[1] and xCoords[4] >= xCoords[2]:
	fout.write(str((xCoords[2] - xCoords[1]) * (yCoords[2] - yCoords[4])))
#check if mower billboard covers bottom part of billboard
elif yCoords[3] < yCoords[2] and xCoords[3] <= xCoords[1] and yCoords[4] >= yCoords[2] and xCoords[4] >= xCoords[2]:
	fout.write(str((xCoords[2] - xCoords[1]) * (yCoords[3] - yCoords[1])))
#check if mower billboard covers left part of billboard
elif xCoords[4] > xCoords[1] and xCoords[3] <= xCoords[1] and yCoords[4] >= yCoords[2] and yCoords[3] <= yCoords[1]:
	fout.write(str((xCoords[2] - xCoords[4]) * (yCoords[2] - yCoords[1])))
#check if mower billboard covers right part of billboard
elif xCoords[3] < xCoords[2] and xCoords[4] >= xCoords[2] and yCoords[4] >= yCoords[2] and yCoords[3] <= xCoords[1]:
	fout.write(str((xCoords[3] - xCoords[1]) * (yCoords[2] - yCoords[1])))
#otherwise, mower billboard only covers a portion of the billboard
else:
	fout.write(str((xCoords[2] - xCoords[1]) * (yCoords[2] - yCoords[1])))
