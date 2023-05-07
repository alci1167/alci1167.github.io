#input
cow_num = int(input())
cows = []
for _ in range(cow_num):
    x, y = map(int, input().split())
    cows.append((x, y))

#coordinate compression to reduce the range of x and y values
seen_x, seen_y = set(), set()
for c in cows:
    assert not (c[0] in seen_x or c[1] in seen_y)  #make sure we haven't seen this coordinate before
    seen_x.add(c[0])
    seen_y.add(c[1])

#sort cows by x coordinate and assign new compressed x coordinate to each cow
cows.sort()
reduced_x = {cows[i][0]: i for i in range(cow_num)}

#sort cows by y coordinate and assign a new compressed y coordinate to each cow
cows.sort(key=lambda c: c[1])
reduced_y = {cows[i][1]: i for i in range(cow_num)}

#update the coordinates with the compressed
for i in range(cow_num):
    x, y = cows[i]
    cows[i] = (reduced_x[x], reduced_y[y])

#sort cows by their compressed x coordinate
cows.sort()

#compute prefix sums for y lines
lt_y = [[0] * (cow_num + 1) for _ in range(cow_num)]  #number of cows below or equal to y coordinate in column x
gt_y = [[0] * (cow_num + 1) for _ in range(cow_num)]  #number of cows above or equal to y coordinate in column x
for c in range(cow_num):
    curr_y = cows[c][1]
    for x in range(1, cow_num + 1):
        lt_y[curr_y][x] = lt_y[curr_y][x - 1] + (cows[x - 1][1] < curr_y)
        gt_y[curr_y][x] = gt_y[curr_y][x - 1] + (cows[x - 1][1] > curr_y)

#count number of boxes that contain at least two cows
total = 0
for c1 in range(cow_num):
    for c2 in range(c1 + 1, cow_num):
        bottom = min(cows[c1][1], cows[c2][1])
        top = max(cows[c1][1], cows[c2][1])
        bottom_total = 1 + lt_y[bottom][c2 + 1] - lt_y[bottom][c1]  #number of cows below or equal to bottom in the rectangle
        top_total = 1 + gt_y[top][c2 + 1] - gt_y[top][c1]  #number of cows above or equal to top in the rectangle
        total += bottom_total * top_total

#count number of boxes that contain only one cow or none at all
total += cow_num + 1

print(total)
