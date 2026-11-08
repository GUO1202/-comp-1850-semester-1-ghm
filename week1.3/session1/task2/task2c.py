# Week 1.3, Session 1: Task 2c

with open('file_data.txt', 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            break
        print(char)

# We do not know the file length in advance. Keep reading until
# read(1) returns an empty string at the end of the file.
