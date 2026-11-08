# Week 1.3, Session 2: Word Counter

filename = input("Enter the file name: ")
try:
    with open(filename, 'r') as f:
        content = f.read()
    print(f"Word count: {len(content.split())}")
except OSError:
    print("Could not open the file")
