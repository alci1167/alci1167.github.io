with open("milkvisits.in") as read:
    farmNum, queryNum = [int(i) for i in read.readline().split()] #read first line to get number of farms and queries

    farms = read.readline() #read second line to get the type of milk produced by each farm
    neighbors = [[] for _ in range(farmNum)] #read remaining lines to get the tree structure
    for f in range(farmNum - 1):
        f1, f2 = [int(i) - 1 for i in read.readline().split()]
        neighbors[f1].append(f2)
        neighbors[f2].append(f1)

    #read the queries from the remaining lines
    queries = []
    for _ in range(queryNum):
        query = read.readline().split()
        query[0], query[1] = int(query[0]) - 1, int(query[1]) - 1
        queries.append(query)

#process through tree and find different components
componentNum = 0
component = [-1 for _ in range(farmNum)]
for f in range(farmNum):
    #if current farm has already been visited we skip it
    if component[f] != -1:
        continue
    frontier = [f]
    currentType = farms[f]
    while frontier:
        curr = frontier.pop()
        #we assign the current component number to the farm
        component[curr] = componentNum
        for n in neighbors[curr]:
            #we can visit a neighbor if it's new and is of the same type
            if farms[n] == currentType and component[n] == -1:
                frontier.append(n)
    #increment the component number for next connected component
    componentNum += 1

with open("milkvisits.out", "w") as written:
    for a, b, milk in queries:
        #if farms a and b are in the same component, output 1 if they produce the same type of milk, and 0 otherwise
        if component[a] == component[b]:
            if farms[a] == milk:
                print(1, end="", file=written)
            else:
                print(0, end="", file=written)
        #if farms a and b are in different components, output 1 since they will both be visited
        else:
            print(1, end="", file=written)
    print(file=written)
