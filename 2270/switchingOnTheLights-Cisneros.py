import sys

#set the recursion limit to prevent stack overflow during floodfill
sys.setrecursionlimit(100000)

#read input
fileIn = open("lightson.in", "r")
N, m = map(int, fileIn.readline().split())

#initialize variables
lit_rooms = 1
visited = [[False for i in range(N)] for j in range(N)]
litUp = [[False for i in range(N)] for j in range(N)]
switches = [[[] for i in range(N)] for j in range(N)]

#parse switch info from input file and store in switches matrix
for i in range(m):
    x, y, a, b = map(int, fileIn.readline().split())
    switches[x - 1][y - 1].append((a - 1, b - 1))

#check if a room is connected to other lit up room
def check_connected(x, y):
    dir_x = [-1, 0, 1, 0]
    dir_y = [0, -1, 0, 1]

    for i in range(4):
        new_x = x + dir_x[i]
        new_y = y + dir_y[i]

        #if adjacent room is out of bounds, we skip it
        if new_x < 0 or new_y < 0 or new_x > N - 1 or new_y > N - 1:
            continue

        #if adjacent room is already lit up return true
        if visited[new_x][new_y]:
            return True

    #if none of the adjacent rooms are lit up return false
    return False

#floodfill algorithm to find number of lit-up rooms
def floodFill(x, y):
    global lit_rooms

    #if current room is out of bounds, already visited, or not lit up, return
    if (
        x < 0
        or y < 0
        or x > N - 1
        or y > N - 1
        or visited[x][y]
        or not litUp[x][y]
    ):
        return

    #if current room is not connected to any other lit up room and is not the starting room, return
    if not check_connected(x, y) and not (x == 0 and y == 0):
        return

    #mark current room as visited and lit up
    visited[x][y] = True

    #recursively call floodfill on adjacent rooms
    dir_x = [-1, 0, 1, 0]
    dir_y = [0, -1, 0, 1]
    for i in range(4):
        floodFill(x + dir_x[i], y + dir_y[i])

    #toggle lights in all rooms controlled by switches in the current room
    for i in range(len(switches[x][y])):
        room_x = switches[x][y][i][0]
        room_y = switches[x][y][i][1]

        #if room is not lit up, we increment lit_rooms and mark as lit up
        if not litUp[room_x][room_y]:
            lit_rooms += 1
        litUp[room_x][room_y] = True

        #recursively call floodfill on new lit up room
        floodFill(room_x, room_y)

#mark starting room at (0,0) as lit up
litUp[0][0] = True

#call floodfill on starting room to begin algorithm
floodFill(0, 0)

print(lit_rooms, file=open("lightson.out", "w"))