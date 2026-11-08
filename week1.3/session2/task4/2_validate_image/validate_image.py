# Week 1.3, Session 2: Validate image

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
    valid = True
    if width <= 0 or any(len(row) != width for row in pixels):
        print("Invalid width")
        valid = False
    if height <= 0 or len(pixels) != height:
        print("Invalid height")
        valid = False
    if max_gray <= 0 or max_gray > 65535 or any(pixel < 0 or pixel > max_gray for row in pixels for pixel in row):
        print("Invalid pixel values")
        valid = False
    if valid:
        print("Valid image")
except OSError:
    print("Could not open or write the file")
except (ValueError, IndexError):
    print("Invalid PGM format")
