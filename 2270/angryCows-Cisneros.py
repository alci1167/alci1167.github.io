with open("angry.in", "r") as infile:

    #assigns the first line of values from the input file to n and k
    n, k = map(int, infile.readline().split())
    #assigns n number of flies from the input file to bales 
    bales = [int(infile.readline()) for _ in range(n)]
    #sorts the bales list
    bales.sort()

#we can use a function to find the min blast radius to blow up all the haybales
def min_blast_radius(bales, k):

    #we can set the left bound of the binary search to 0 and the right bound to the max  blast radius
    left, right = 0, bales[-1] - bales[0]
    
    #do binary search until the left and right bounds meet
    while left < right:
        #midpoint between the left and right bounds
        mid = (left + right) // 2
        #if blast radius at the midpoint is valid, move right bound to midpoint
        if is_valid_blast_radius(bales, k, mid):
            right = mid
        #if blast radius at the midpoint is not valid, move left bound to midpoint and add 1
        else:
            left = mid + 1
    return left

#we can use another function to check whether a blast radius can blow up all the haybales
def is_valid_blast_radius(bales, k, blast_rad):

    #set last blast location to negative infinity 
    last_blast_location = -float("inf")
    needed_cows = 0

    #we iterate through the haybales
    for bale_pos in bales:
        #if the current haybale is outside the blast radius of the last cow, we need another cow
        if abs(bale_pos - last_blast_location) > blast_rad:
            needed_cows += 1
            #we then set the blast location of the current cow to the left bound of the current haybale's blast radius
            last_blast_location = bale_pos + blast_rad
            #if the number of cows needed is larger than k, we return false
            if needed_cows > k:
                return False
            
    #if all the haybales can be blown up we return true
    return True

#we can call the min_blast_radius function with the bales list and k as arguments
ans = min_blast_radius(bales, k)

with open("angry.out", "w") as outfile:
    outfile.write(str(ans) + "\n")