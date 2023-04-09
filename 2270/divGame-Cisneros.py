#take input from user
n = int(input())

#initialize variable to count number of divisors
ans = 0

#loop over all numbers p between 2 and the square root of n
for p in range(2, int(n**0.5) + 1):

    #count the number of times p divides n
    e = 0
    while n % p == 0:
        #divide n by p as many times as possible
        n //= p
        #increment exponent count
        e += 1
    
    #count the number of divisors that have exponents 1 to p that divides n
    i = 1
    while e >= i:
        #subtract i from e and add 1 to divisor count, and increment i
        e -= i
        ans += 1
        i += 1

#if n is still greater than 1, it means n is a prime factor of the original number,
#so add 1 to the divisor count
ans += n > 1

#print final number of divisors
print(ans)