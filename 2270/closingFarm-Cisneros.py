import sys

sys.stdin = open("closing.in", "r")
sys.stdout = open("closing.out", "w")

#read in the number of nodes and edges from input file
n, m = map(int, input().split())

#adjacency list and order list
adj, order = {}, []
for i in range(1, n + 1):
    adj[i] = []

#visited and closed lists
visited, closed = [False] * (n + 1), [False] * (n + 1)

#nodes counter
nodes = 0

#recursive DFS function
def dfs(node):
    global nodes
    #if node has already been visited or closed, return
    if visited[node] or closed[node]:
        return
    #otherwise, mark node as visited and add 1 to the nodes counter
    nodes += 1
    visited[node] = True
    #recursively visit all unvisited adjacent nodes
    for u in adj[node]:
        if not visited[u]:
            dfs(u)

#read in the edges and add them to the adj list
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

#read in the order of nodes to be closed
for i in range(n):
    order.append(int(input()))

#check if the original graph is connected
dfs(1)
if nodes == n:
    print("YES")
else:
    print("NO")

#check if closing each node in order gives a disconnected graph
for i in range(n - 1):
    #initialize new visited list and nodes counter
    visited = [False] * (n + 1)
    nodes = 0
    #mark the current node as closed
    closed[order[i]] = True
    #dfs starting from the last node in order
    dfs(order[n - 1])
    #check if remaining nodes are connected
    if nodes == n - i - 1:
        print("YES")
    else:
        print("NO")
