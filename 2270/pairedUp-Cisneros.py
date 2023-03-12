read = open("pairup.in", "r").readline

#assign # of cows  
n = int(read())

#empty list to store cows and milk output
cows = []

#assigning the cow count and milk output to cows list in pairs like (milk output, cow count)
for i in range(n):
    x, y = map(int, read().split())
    cows.append((y, x)) 
    
cows.sort()  #sort based on milk output

#we can use two pointers to pair the cows with the most and least milk output
left = 0  #pointer to the leftmost unpaired cow
right = n - 1  #pointer to the rightmost unpaired cow
time = 0  #max time for milking in all pairs

while left <= right:
    #we can calculate the milking time for the pair of cows
    pair_time = cows[left][0] + cows[right][0]
    time = max(time, pair_time) #update the time
    
    #update the cow counts
    if cows[left][1] == cows[right][1]: #if the cow counts are equal, they are paired up and we can move the pointers by one
        left += 1
        right -= 1
    elif cows[left][1] < cows[right][1]: #if left cow count is smaller than right cow count, we can subtract left count from right count
        cows[right] = (cows[right][0], cows[right][1] - cows[left][1])
        left += 1 #move left pointer by one
    else: #if left cow count is greater than right cow count, we can subtract right count from left count
        cows[left] = (cows[left][0], cows[left][1] - cows[right][1])
        right -= 1 #move right pointer to previous one

print(time, file=open('pairup.out', 'w'))