import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]


n_names = int(input("how many names you want: "))
chosen_names = random.sample(names, n_names)

for name in chosen_names:
    print(name)


# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

# Display the chosen names, one per line
