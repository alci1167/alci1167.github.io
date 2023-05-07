#read input values
inList = [int(i) for i in input().split()]
N, M = inList[0], inList[1]

#coordinates and max temperatures of each stall
cows = list()
for i in range(N):
    t = [int(i) for i in input().split()]
    cows.append(t)

#cooling range and cost of each air conditioner
AC = list()
for i in range(M):
    t = [int(i) for i in input().split()]
    AC.append(t)

#function to apply the air conditioner settings
def applyAC(k: int):
    stalls = [0]*101  #keep track of the temperature of each stall
    s = "{0:010b}".format(k)  #convert the binary string to a 10-digit binary string
    s = s[::-1]  #reverse the order of the bits to iterate better
    cost = 0  #keep track of the total cost of using the air conditioners
    for i in range(10):  #iterate through all air conditioners
        if s[i] == '1':  #if the ith bit is 1, turn on the ith air conditioner
            cost += AC[i][3]  #add the cooling cost of the ith air conditioner to the total cost
            for j in range(AC[i][0], AC[i][1]+1):  #update temperature of all the stalls in the cooling range of the ith air conditioner
                stalls[j] += AC[i][2]

    for i in range(N):  #check if the temperature of each stall is at most the maximum allowed temperature
        for j in range(cows[i][0], cows[i][1]+1):
            if stalls[j] < cows[i][2]:  #if the temperature of the jth stall is less than the maximum allowed temperature, return a large value
                return 10001

    return cost  #return total cost of using the air conditioners

#try all possible combinations of air conditioner settings
x = pow(2, M)
minCost = 10001  #initialize minimum cost to a large value
for i in range(x):
    cost = applyAC(i)  #compute cost of using the ith combination of air conditioner settings
    if cost != 10001:  #if all stalls have temperature at most the maximum allowed temperature, update minimum cost
        minCost = min(minCost, cost)

print(f'{minCost}')
