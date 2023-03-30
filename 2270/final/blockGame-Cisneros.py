from typing import List   # import List type from the typing module

def count_freq(s: str) -> List[int]:
	# this function takes a string s and returns a list of 26 integers representing the frequency of each letter (a-z) in s
	freq = [0] * 26   # initialize a list of 26 integers with value 0
	for c in s:
		freq[ord(c) - ord("a")] += 1   # increment the frequency of the letter at index ord(c) - ord("a") in freq
	return freq   # return the list of frequencies

with open("blocks.in") as read:
	# open the input file "blocks.in" and read the number of words n
	n = int(read.readline())
	# read the n words as a list of pairs into the variable words
	words = [read.readline().split() for _ in range(n)]

max_blocks = [0] * 26   # initialize a list of 26 integers with value 0
for w1, w2 in words:    # iterate over each pair of words in words
	freq1, freq2 = count_freq(w1), count_freq(w2)   # calculate the frequency of letters in each word using count_freq
	for c in range(26):   # iterate over the indices of max_blocks (0-25)
		max_blocks[c] += max(freq1[c], freq2[c])   # add the maximum frequency of the letter at index c in freq1 and freq2 to max_blocks[c]

with open("blocks.out", "w") as written:
	# open the output file "blocks.out" for writing
	for i in max_blocks:
		print(i, file=written)   # write each element of max_blocks to the output file
