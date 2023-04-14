import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

#initialize pre and suf lists
pre = [0] * n  #store the length of the maximum left-subarray ending at i
suf = [0] * (n + 1)  #store the length of the maximum right-subarray starting at i

ans = 0
q = []  #stack to store elements and indices

#loop to calc pre array
for i in range(n):
    while q and q[-1][0] >= a[i]:  #pop elements from stack until a[i] is greater
        q.pop()
    x = -1
    if q:  #get the index of the top element in the stack
        x = q[-1][1]
    pre[i] = 1 + i - x - 1  #calc the length of left-subarray ending at i
    q.append((a[i], i))  #push current element and its index to stack

q = []  #clear the stack

# Loop to calculate suf array
for i in range(n - 1, -1, -1):  #iterate backwards from n-1 to 0
    while q and q[-1][0] >= a[i]:  #pop elements from stack until a[i] is greater
        q.pop()
    x = n
    if q:  #get index of the top element in the stack
        x = q[-1][1]
    suf[i] = 1 + x - i - 1  #calculate the length of right-subarray starting at i
    q.append((a[i], i))  #push current element and its index to stack
    ans = max(ans, (pre[i] + suf[i] - 1) * a[i])  #calculate the maximum area

print(ans)
