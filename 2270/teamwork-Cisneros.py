#open input file and read in the values
with open("teamwork.in") as read:
    #read  first line for contains N and K
    N, K = map(int, read.readline().split())
    #read the next N lines for cow values
    cows = [int(read.readline()) for _ in range(N)]

    #initialize dp table with -1 for all entries except the first
    dp = [cows[0]] + [-1] * (N - 1)

#compute dp table
for i in range(1, N):
    #initialize maximum cow value for the current range to the cow value at index i
    curr_max = cows[i]
    
    #try all possible ranges of cows from i to i-k
    for k in range(K):
        j = i - k
        #if j is less than 0 the range of cows goes before beginning of the list
        if j < 0:
            #break out of the loop since no more valid ranges are left
            break
        #update current maximum cow value to be the maximum of the previous max and the cow value at index j
        curr_max = max(curr_max, cows[j])
        #if j is 0 the current range covers the first cow in the list
        if j == 0:
            #set the value in the dp table for index i to be the maximum value so far
            dp[i] = max(dp[i], curr_max * (k + 1))
        else:
            #update the value in the dp table for index i to be the maximum value so far
            dp[i] = max(dp[i], dp[j - 1] + curr_max * (k + 1))

#maximum value in the dp table 
with open("teamwork.out", "w") as outfile:
    outfile.write(str(dp[-1]) + "\n")
