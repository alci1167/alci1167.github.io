#open input file and read n and m values
with open('hayfeast.in', 'r') as fin:
    n, m = map(int, fin.readline().split())
    #read flavor and spiciness values and store them in a list of tuples
    haybales = [tuple(map(int, line.split())) for line in fin]
    
#initialize left and right pointers to 0 and create an empty list to store maximum spiciness values
left = 0
right = 0
spicyArray = []

#loop while both pointers are less than the number of haybales
while left < n and right < n:
    #initialize flavor sum to 0 and loop through the interval of haybales to find the sum
    flavor = 0 
    for i in range(left, right+1):
        flavor = flavor + haybales[i][0]
    #if the current intervals flavor sum is less than the minimum m, we move the right pointer to the next haybale
    if flavor < m:
        right += 1
    #if the current intervals flavor sum is greater than or equal minimum m, we compute the maximum spiciness value in the interval
    else:
        maxSpicy = 0
        window = right - left
        tempSpicy = []
        for i in range(left, right+1):
            tempSpicy.append(haybales[i][1])
        maxSpicy = max(tempSpicy)
        #add the maximum spiciness value to spicyArray list and move the left pointer to the next haybale
        spicyArray.append(maxSpicy)
        left +=1

with open('hayfeast.out', 'w') as fout:
    fout.write(str(min(spicyArray)) + '\n')