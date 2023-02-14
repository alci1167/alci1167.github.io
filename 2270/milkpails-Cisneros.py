with open('pails.in') as fin:
	buck1, buck2, order = map(int, fin.readline().split())  #reads input file and assigns the values. 

outvar = 0

for first in range(order + 1): #this checks all numbers from 0 -> 77
	x = buck1 * first #for 0-77 we can multiply 17 times each index of order. 
	if x > order: #we can then compare the product to 77 and if its too large we can stop the loop
		break
	
	for second in range(order + 1): #this checks all numbers from 0 -> 77
		current = (buck1 * first) + (buck2 * second) #current is adding a multpiles of 17 and multples of 25 
		if current > order: #if this value is larger than 77 stop the loop. 
			break
		outvar = max(outvar, current) #the outpu value is the max between our largest value under 77 and 0. 
print(outvar, file=open('pails.out', 'w'))
