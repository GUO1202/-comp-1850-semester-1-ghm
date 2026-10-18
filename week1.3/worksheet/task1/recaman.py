# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

sequence = [] # this is the data structure you will use to store the sequence
for n in range(L):
    if n == 0:
        sequence.append(0)
    else:
        next_value = sequence[n-1] - n
        if next_value > 0 and next_value not in sequence:
            sequence.append(next_value)
        else:
            sequence.append(sequence[n-1] + n)


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence