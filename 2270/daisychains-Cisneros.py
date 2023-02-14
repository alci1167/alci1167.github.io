n = int(input())

flowers = list(map(int, input().split()))

photos = 0
for i in range(n): 
	for j in range(i, n): #from i to n
		avgPetals = sum(flowers[i:j + 1]) / (j - i + 1) #for each photo we can make a combination of 2 integers (i and j). we ca

		for index in range(i, j + 1): #from i to j +1
			if flowers[index] == avgPetals: #if a flower has average number of petals, increase photos by 1
				# we found an average flower
				photos += 1
				break

print(photos)