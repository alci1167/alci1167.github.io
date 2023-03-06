with open("maxcross.in") as read:
  #assign values from first line of input file n, k, b
	n, k, b = map(int, read.readline().split())
 
  #seen is array full of zeros 11 long
	seen = [0] * (n + 1)
 
	left, right = 1, k
	value = 0
  #add a 1 to index from the ID
	for _ in range(b):
		seen[int(read.readline())] = 1

#add the values of the seen list to value from indices 1 to k+1 
for i in range(left, right + 1):
  value += seen[i]

#possible is a list of value
answer = [value]

while n > right:
  #add the value of the right +1 index and subtract the value of the left index
  value += seen[right + 1] - seen[left]
  #add 1 to each
  left, right = left + 1, right + 1
  #append the value to possible list
  answer.append(value)

#find the lowest
print(min(answer), file=open("maxcross.out", "w"))