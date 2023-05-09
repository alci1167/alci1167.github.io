with open('wormsort.in', 'r') as f:
    cow_num, wormhole_num = map(int, f.readline().split())

    #read second line and convert the list of cow IDs to 0 indexed values
    cows = list(map(int, f.readline().split()))
    cows = [c - 1 for c in cows]

    #set up adjacency list to represent graph of cows and wormholes
    neighbors = [[] for _ in range(cow_num)]

    #find maximum wormhole width (initialize to 0)
    max_width = 0

    #read remaining lines and add each wormhole to adjacency list
    for _ in range(wormhole_num):
        c1, c2, width = map(int, f.readline().split())
        c1 -= 1
        c2 -= 1
        neighbors[c1].append((c2, width))
        neighbors[c2].append((c1, width))
        max_width = max(max_width, width)

#set up binary search bounds for the maximum wormhole width
lo = 0
hi = max_width + 1

#initialize valid to store the valid maximum wormhole width
valid = -1

#binary search until bounds converge
while lo <= hi:
    mid = (lo + hi) // 2

    #assign each cow to a connected component using BFS, we can ignore edges below current wormhole width
    component = [-1] * cow_num
    curr_comp = 0
    for c in range(cow_num):
        if component[c] != -1:
            continue
        frontier = [c]
        while frontier:
            curr = frontier.pop()
            component[curr] = curr_comp
            for n, w in neighbors[curr]:
                if component[n] == -1 and w >= mid:
                    frontier.append(n)
        curr_comp += 1

    #check if all cows are in the same connected component as wanted final position
    sortable = all(component[c] == component[cows[c]] for c in range(cow_num))

    #if all cows are sortable, we can update valid maximum wormhole width and search for a larger value
    if sortable:
        valid = mid
        lo = mid + 1
    #if not all cows are sortable, we search for a smaller value
    else:
        hi = mid - 1

#valid maximum wormhole width or -1 if there is none
with open('wormsort.out', 'w') as f:
    f.write(str(valid) if valid != max_width + 1 else "-1" + "\n")
