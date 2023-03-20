#open the input file and read in the number of cows
with open("moocast.in") as read:
    cow_num = int(read.readline())

    #store the x and y coordinates aswell as the transmission power of each cow
    x = [0 for _ in range(cow_num)]
    y = [0 for _ in range(cow_num)]
    power = [0 for _ in range(cow_num)]

    #read in coordinates and power of each cow from input file
    for c in range(cow_num):
        x[c], y[c], power[c] = [int(i) for i in read.readline().split()]

#create boolean list to store which cows can communicate with each other
connected = [[False for _ in range(cow_num)] for _ in range(cow_num)]

#populate the connected list by checking the distance between each pair of cows
for i in range(cow_num):
    for j in range(cow_num):
        #calculate the distance squared between cows i and j
        dist_squared = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        #if the distance is less than or equal to the transmission power of cow i, the two cows are connected
        connected[i][j] = dist_squared <= power[i] ** 2

#recursive function to find the number of cows reachable by a given cow
def reachable_cows(c: int) -> int:
    #we can use the visited list to keep track of which cows have been visited
    global visited
    visited[c] = True
    #we will start with count of 1, since we can reach the initial cow c
    reached = 1
    #recursively check each cow that is connected to the current cow and hasn't been visited yet
    for nc in range(cow_num):
        if not visited[nc] and connected[c][nc]:
            visited[nc] = True
            #we can add the number of cows reachable from the connected cow to our count
            reached += reachable_cows(nc)
    return reached

#variable to store the maximum number of reachable cows
max_cows = 0
#iterate through each cow
for c in range(cow_num):
    #we can use the visited list to keep track of which cows have been visited
    visited = [False for _ in range(cow_num)]
    #we find the number of cows reachable from the current cow
    max_cows = max(max_cows, reachable_cows(c))

print(max_cows, file=open("moocast.out", "w"))