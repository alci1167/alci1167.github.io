from typing import List   #import List type from the typing module

def count_freq(s: str) -> List[int]:#this function takes a string and returns a list of 26 integers that represents the frequency of each letter (a-z)
	freq = [0] * 26   #initialize a list of 26 integers with value 0
	for c in s:
		freq[ord(c) - ord("a")] += 1   #increment the frequency of the letter at index ord(c) - ord("a") in freq
	return freq   #return the list of frequencies

with open("blocks.in") as read:
	#open the input file and read the number of words n
	n = int(read.readline())
	#read the n words as a list of pairs into the variable words
	words = [read.readline().split() for _ in range(n)]

maxBlocks = [0] * 26   #initialize a list of 26 integers with value 0
for word1, word2 in words:    #iterate through each pair of words in words
	freq1, freq2 = count_freq(word1), count_freq(word2)   #calc the frequency of letters in each word using count_freq
	for _ in range(26):   #iterate through the indices of max_blocks 0-25
		maxBlocks[_] += max(freq1[_], freq2[_])   #add the max frequency of the letter at index c in freq1 and freq2 to max_blocks[c]

with open("blocks.out", "w") as written:
	for i in maxBlocks:
		print(i, file=written)   #write each element of max_blocks to the output file
