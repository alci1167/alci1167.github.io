from collections import deque

#read input from the input file
with open("shuffle.in", "r") as input_file:
    n = int(input_file.readline())  #number of cows

    #list a represents initial ordering of the cows
    a = list(map(int, input_file.readline().split()))

    #initialize list to keep track of the number of cows that each position will receive after one shuffle
    cowsShuffle = [0] * n

    #calc number of cows that a position will receive after one shuffle
    for i in range(n):
        a[i] -= 1  # Convert 1-based indexing to 0-based indexing
        cowsShuffle[a[i]] += 1

    #initialize ans to keep track of the number of positions that will receive at least one cow after all shuffles
    ans = n

    #we use a deque to keep track of positions that are empty after one shuffle
    noCows = deque()

    #calc positions that are empty after one shuffle.
    for i in range(n):
        if cowsShuffle[i] == 0:
            noCows.append(i)  #add the empty position to deque
            ans -= 1  #decrement ans since the empty position will not receive any cows after all shuffles

    #process the empty positions in the deque
    while noCows:
        curr = noCows.popleft()  #we can get the next empty position from the deque

        #position curr can't contribute any cows
        cowsShuffle[a[curr]] -= 1

        #if a[curr] has no cows, we insert it into the deque
        if cowsShuffle[a[curr]] == 0:
            noCows.append(a[curr])  #add the empty position to the deque
            ans -= 1  #decrement ans since the empty position will not receive any cows after all shuffles

with open("shuffle.out", "w") as output_file:
    print(ans, file=output_file)
