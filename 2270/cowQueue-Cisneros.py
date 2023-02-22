import sys

sys.stdin = open('cowqueue.in')

n = int(input()) #we assign the first value of our input file to n

cows = [] #empty list

for i in range(n): #iterate through n number of times and split data from input file to cows list
	cows.append(list(map(int, input().split())))

cows.sort() #using the sort function, we can sort cows

cur_time = 0 #output

for c in cows: #iterate through cows
	if cur_time > c[0]: #if cur_time is more than first value of the last list in cows
		cur_time += c[1] #add the other value to cur_time
	else:
		#the last cow finished before the second to last one
		#we can set curr_time to when this cow finishes
		cur_time = c[0] + c[1]

print(cur_time, file=open('cowqueue.out', 'w'))