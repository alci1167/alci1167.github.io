with open("berries.in") as read:
	#read first line and split into n and k
	n, k = map(int, read.readline().split())
	#read the second line and split into list of n integers
	berries = [*map(int, read.readline().split())]

#initialize ans to store max number of berries that can be collected
ans = 0

#iterate through a xc  l possible numbers of berries that can be collected
for i in range(1, max(berries) + 1):
	#modulo value to i
	mod = i
	#initialize full and temp to count number of full buckets and total number of berries in buckets
	full = 0 
	temp = 0

	#iterate through all buckets of berries
	for j in range(n):
		#add number of full buckets that can be made with current modulo
		full += berries[j] // mod

	#if number of full buckets is less than half of the total wanted buckets, we cant collect enough berries
	if full < k / 2:
		break

	#if we can collect enough berries to fill all the buckets, we can set max number of berries
	if full >= k:
		ans = max(ans, (k // 2) * i)
		continue

	#calc maximum number of berries we can collect
	x = (full - k // 2) * i
 
	#sort berries by modulo in descending order
	berries.sort(key=lambda x: (x % mod), reverse=True)

	#add largest berries that have the same modulo value until we have enough berries
	while temp < (k - full):
		if temp < len(berries):
			x += berries[temp] % mod
			temp += 1
		else:
			break

	#max number of berries to collect
	ans = max(ans, x)

print(ans, file=open("berries.out", "w"))
