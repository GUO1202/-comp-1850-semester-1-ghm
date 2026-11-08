# Week 1.3, Additional work: Frequency Analysis

filename = input("Enter the file name: ")
try:
    with open(filename, 'r') as f:
        content = f.read().lower()
    frequency = {}
    for ch in content:
        if ch.isalpha():
            frequency[ch] = frequency.get(ch, 0) + 1
    print(frequency)
except OSError:
    print("Could not open the file")
