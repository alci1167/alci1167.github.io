n = int(input())
base = [0] * (n+1)
items = [[] for _ in range(n+1)]

with open('dishes.in', 'r') as fin:
    for i in range(n):
        x = int(fin.readline().strip())
        # impossible to add this plate
        if x < len(items) and x < items[x][-1]:
            ans = i
            break
        # plates that go on this stack
        for j in range(x, 0, -1):
            if not base[j]:
                base[j] = x
        # remove plates with smaller labels
        while items[base[x]] and items[base[x]][-1] < x:
            placed = items[base[x]].pop()
        # add this plate to the stack
        items[base[x]].append(x)

with open('dishes.out', 'w') as fout:
    fout.write(str(ans) + '\n')
