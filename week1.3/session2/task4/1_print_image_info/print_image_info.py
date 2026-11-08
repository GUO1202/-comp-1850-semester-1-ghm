# Week 1.3, Session 2: Print PGM image info

filename = input("Enter the PGM file name (e.g. ../images/feep.pgm): ")
try:
    with open(filename, 'r') as f:
        data = []
        for line in f:
            line = line.split('#')[0].strip()
            if line:
                data.append(line)
    if data[0] != 'P2':
        raise ValueError("Invalid PGM format")
    width, height = [int(i) for i in data[1].split()]
    max_gray = int(data[2])
    pixels = [[int(i) for i in line.split()] for line in data[3:]]
    print(f"Dimensions: {width} x {height} pixels")
    print(f"Max Gray Value: {max_gray}")
except OSError:
    print("Could not open or write the file")
except (ValueError, IndexError):
    print("Invalid PGM format")
