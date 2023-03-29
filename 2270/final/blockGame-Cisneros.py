with open("blocks.in", "r") as fin:
    # Read the number of words.
    n = int(fin.readline().strip())

    # Initialize a dictionary to store the maximum number of times each letter appears in the blocks.
    blocks = {}

    # Read each pair of words and update the blocks dictionary.
    for i in range(n):
        word1, word2 = fin.readline().strip().split()
        for letter in "abcdefghijklmnopqrstuvwxyz":
            blocks[letter] = max(blocks.get(letter, 0), max(word1.count(letter), word2.count(letter)))

with open("blocks.out", "w") as fout:
    # Write the maximum number of blocks for each letter to the output file.
    for letter in "abcdefghijklmnopqrstuvwxyz":
        fout.write(str(blocks[letter]) + "\n")
