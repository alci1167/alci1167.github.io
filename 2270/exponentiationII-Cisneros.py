MOD = 10**9 + 7

#function to implement binary exponentiation
def exp(x, n, m):
    #check that n is not negative
    assert n >= 0
    #reduce x modulo m
    x %= m
    #initialize result to 1
    res = 1
    #repeat until n is zero
    while n > 0:
        #if n is odd, multiply result by x modulo m
        if n % 2 == 1:
            res = res * x % m
        #square x modulo m and halve n
        x = x * x % m
        n //= 2
    #return result
    return res

#read the number of test cases from input
t = int(input())
#loop over the test cases
for i in range(t):
    #read the values of a, b, and c from input
    a, b, c = map(int, input().split())
    #compute b^c modulo (MOD-1) using exp function
    pow_bc = exp(b, c, MOD-1)
    #compute a^(b^c) modulo MOD using exp function
    ans = exp(a, pow_bc, MOD)
    #print the result
    print(ans)
