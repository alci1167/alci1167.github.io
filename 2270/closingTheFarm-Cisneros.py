class DisjointSetUnion:
    def __init__(self, num_nodes: int) -> None:
        #initialize parent array to contain the nodes index itself
        self.parent = [*range(num_nodes)]
        #initialize size array to contain all 1s
        self.size = [1] * num_nodes

    def find_parent(self, v: int) -> int:
        #recursively find parent of the given node
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find_parent(self.parent[v])
        return self.parent[v]

    def union(self, a: int, b: int) -> bool:
        #find parents of the two nodes
        a = self.find_parent(a)
        b = self.find_parent(b)
        #if both nodes are already in the same set, we return False
        if a == b:
            return False
        #merge smaller set into the larger set
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def connected(self, a: int, b: int) -> bool:
        #check if the two nodes are in the same set
        return self.find_parent(a) == self.find_parent(b)
    
with open("closing.in", "r") as infile:
    #read in the number of nodes and edges
    n, m = map(int, infile.readline().split())
    #initialize adjacency list for the graph
    graph = [[] for _ in range(n)]
    #read in each edge and add it to the adjacency list
    for _ in range(m):
        f, t = map(lambda i: int(i) - 1, infile.readline().split())
        graph[f].append(t)
        graph[t].append(f)
    #read in order in which nodes are removed
    remove_order = [int(infile.readline()) - 1 for _ in range(n)]

dsu = DisjointSetUnion(n)

open_barns = set()
components = 0
fully_connected = []

for node in remove_order[::-1]:
    #add current node to the graph
    components += 1
    #check its neighbors to see if any can be connected to it
    for adj in graph[node]:
        if adj in open_barns:
            #connect the nodes if not already connected
            if dsu.union(adj, node):
                components -= 1
    #check if the graph is still connected
    fully_connected.append("YES" if components == 1 else "NO")
    #add current node to the set of open nodes
    open_barns.add(node)

print(*fully_connected[::-1], sep="\n", file=open("closing.out", "w"))
