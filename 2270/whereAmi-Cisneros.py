file_in = open('whereami.in')
data = file_in.read().strip().split('\n') #we are reading input data and spliting it by line
n = int(data[0]) #the first line is assigned to n
mailboxes = data[1] #the second line is assigned to mailboxes

ans = 0

for k in range(1, n+1): #iterate through 1 to n+1 excluding n+1

    sequence = set()

    for i in range(n-k+1): #using k we can compare all pairs of substrings. As k increases the number of substrngs decreases 
        sequence.add(mailboxes[i : i+k]) #using i we can populate sequence to see the substring of unique letters
    
    if len(sequence) == (n-k+1):#if the length of sequence after the for loop is equal to n-k+1 then we havve an answer
        ans = k
        break

print(ans, file = open('whereami.out','w'))
