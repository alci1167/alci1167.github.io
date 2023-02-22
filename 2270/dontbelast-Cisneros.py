fin, fout = open('notlast.in'), open('notlast.out', 'w')

cows = {} #empty dictionary named cows

#this makes keys for each cows with a 0 mapping value
cows['Bessie'] = 0
cows['Elsie'] = 0
cows['Daisy'] = 0
cows['Gertie'] = 0
cows['Annabelle'] = 0
cows['Maggie'] = 0
cows['Henrietta'] = 0

n = int(fin.readline()) #assigns first value of input file to n
for x in range(n): #iterate through n 
    data = fin.readline().split() #assign input values to corresponding cows 
    cows[data[0]] += int(data[1]) #if a cow produces milk more than once we can add those together

cowList = [(cows[x],x) for x in cows] #we can make a list of the values above. This list has the duration and name for each cow
cowList.sort() #we can then sort the list

min = cowList[0][0] #this helps us find the smallest value 

mincount = 0
min2 = 101 

first = 0 
for cow in cowList: #we can iterate through our list 
    if cow[0] != min: #here we are comparing the total duration of each cow to the min
        if first == 0:
            mincount += 1
            first = 1
            min2 = cow #find the second to smallest 
        elif min2[0] == cow[0]:
            mincount += 1
            min2 = cow #find the second to smallest 

if mincount == 1: #only one cow
    fout.write(min2[1]) #print name of second lowest producing cow
else: #tie
    fout.write('Tie') 