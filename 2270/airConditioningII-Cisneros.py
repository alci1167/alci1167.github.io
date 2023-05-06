# Read input values
in_list = [int(i) for i in input().split()]
N, M = in_list[0], in_list[1]

# Read the coordinates and max temperatures of each stall
cows = list()
for i in range(N):
    t = [int(i) for i in input().split()]
    cows.append(t)

# Read the cooling range and cost of each air conditioner
ac = list()
for i in range(M):
    t = [int(i) for i in input().split()]
    ac.append(t)

# Helper function to apply the air conditioner settings
def apply_ac(k: int):
    stalls = [0]*101  # Keep track of the temperature of each stall
    s = "{0:010b}".format(k)  # Convert the binary string to a 10-digit binary string
    s = s[::-1]  # Reverse the order of the bits for easier iteration
    cost = 0  # Keep track of the total cost of using the air conditioners
    for i in range(10):  # Iterate through all the air conditioners
        if s[i] == '1':  # If the i-th bit is 1, turn on the i-th air conditioner
            cost += ac[i][3]  # Add the cooling cost of the i-th air conditioner to the total cost
            for j in range(ac[i][0], ac[i][1]+1):  # Update the temperature of all the stalls within the cooling range of the i-th air conditioner
                stalls[j] += ac[i][2]

    for i in range(N):  # Check if the temperature of each stall is at most the maximum allowed temperature
        for j in range(cows[i][0], cows[i][1]+1):
            if stalls[j] < cows[i][2]:  # If the temperature of the j-th stall is less than the maximum allowed temperature, return a large value (10001)
                return 10001

    return cost  # Return the total cost of using the air conditioners

# Try all possible combinations of air conditioner settings
x = pow(2, M)
min_cost = 10001  # Initialize the minimum cost to a large value (10001)
for i in range(x):
    cost = apply_ac(i)  # Compute the cost of using the i-th combination of air conditioner settings
    if cost != 10001:  # If the combination is valid (i.e., all stalls have temperature at most the maximum allowed temperature), update the minimum cost
        min_cost = min(min_cost, cost)

# Output the minimum cost
print(f'{min_cost}')
