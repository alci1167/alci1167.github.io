import sys
sys.stdin = open("speeding.in", "r")


#we can assign the first row of values to n and m.
n, m = list(map(int, input().split()))

#since the output file uses the first row to indicate the road segments 
#and bessie segments we can use n and m to split the data into two lists. One for the the speed limit and one for bessie's speed.
speedLimit = [list(map(int, input().split())) for i in range(n)]
bessieSpeed = [list(map(int, input().split())) for i in range(m)]

total = 0

speedL = []
bessieL = [] 

#here we iterate through speedlimit. Since speedLimit has the length and speed we want to append the second number in the 1st position to speedL
for i in speedLimit:
  for j in range(i[0]):
    speedL.append(i[1])
    
#here we iterate through bessiespeed. Since speedLimit has the length and speed we want to append the second number in the 1st position to bessieL
for i in bessieSpeed:
  for j in range(i[0]):
    bessieL.append(i[1])

#here we compare bessie's speed to the speed limit
#if bessie's speed is larger than the speed limit and the diference
#between the two is larger than the total it will be the new total or answer.
#It does this 100 times because of th length of the road. 
for i in range(100):
  if (bessieL[i] > speedL[i]) and (bessieL[i] - speedL[i] > total):
    total = bessieL[i] - speedL[i]


out = open("speeding.out", "w")
out.write(str(total))
out.close()