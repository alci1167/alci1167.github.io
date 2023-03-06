mod = 7

#read in values from input file to cows[]
with open("div7.in") as read:
	cows = [int(read.readline()) for _ in range(int(read.readline()))]
 
photo = 0

#list with -1 at each index, the list is MOD long
first = [-1 for i in range(mod)]
#assign 0 to first index: [0, -1, -1, -1, -1, -1, -1,]
first[0] = 0  

runMod = 0
#we can use enumerate to tell us the index value and the value at that index
for c, v in enumerate(cows):
  #assign the modulo of the values in cows and 7 to runMod
  runMod = (runMod + v) % mod

  # check if the index of runMod is -1 in first[]
  if first [runMod] == -1:
    #assign the index value c to first[]
    first[runMod] = c
    
  else:
    #our output is the max between the lengths of the shortest and longest prefixes
    photo = max(photo, c - first[runMod])

print(photo, file = open("div7.out", "w"))