fin = open('highcard.in')

n = int(fin.readline()) #assigns first line of input file to n
elsie_has = set() #empty set 

#we can add n number of lines from the input file to bessie_has 
for i in range(n): 
    elsie_has.add(int(fin.readline()))

elsie, bessie = [], [] #create empty lists for both elsie and bessie

#from 1 to 2n+1 since range is 1 to n-1
for i in range(1, n * 2 + 1):

  #since we only have the 1 to 2n cards we can iterate through and check if they are in elsie_has.
  #If they are we can add them to the elsie list and if they aren't we add them to the bessie list.
	if i not in elsie_has:
		bessie.append(i)
	else:
		elsie.append(i)

ans, bessie_index, elsie_index = 0, 0, 0

#since both players get n cards we compare the values at each index up to n
while bessie_index < n and elsie_index < n:
  #if bessie has a higher card we add 1 to our ans and increase the index of both by 1
	if bessie[bessie_index] > elsie[elsie_index]:
		ans += 1
		bessie_index += 1
		elsie_index += 1
    #if bessie doesn't have a higher card we compare the ccard of the next index
	else:
		bessie_index += 1

with open('highcard.out', 'w') as f:
    f.write(str(ans) + '\n')