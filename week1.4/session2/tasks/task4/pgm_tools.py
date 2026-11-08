
# PGM functions that we write

def readPGM( filename ):
    ''' 
    Read a named PGM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''

    with open(filename, "r") as f:
        values = []
        for line in f:
            line = line.split('#')[0].strip()
            if line:
                values.extend(line.split())
    if values[0] != "P2":
        raise ValueError("File is not a P2 PGM image")
    width, height = int(values[1]), int(values[2])
    max_gray = int(values[3])
    flat = [int(value) for value in values[4:]]
    if len(flat) != width * height:
        raise ValueError("Pixel count does not match image dimensions")
    pixels = [flat[row * width:(row + 1) * width] for row in range(height)]
    return width, height, max_gray, pixels
    
def writePGM( filename, image ):
    '''
    Write a PGM file to disk
    Input: filename string, image tuple data
    Output: None
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    with open(filename, "w") as f:
        f.write(f"P2\n{width} {height}\n{max_gray}\n")
        for row in pixels:
            f.write(" ".join(str(pixel) for pixel in row) + "\n")

def invertPGM( image ):
    '''
    Invert an image, ie. pixel value = 255 - pixel value
    Input: image data
    Output: inverted image data
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    # your code
    # create a new pixel array of inverted data 
    inverted = [[max_gray - pixel for pixel in row] for row in pixels]
    
    return width,height,max_gray,inverted

# code to test the PGM functions

image = readPGM("images/feep.pgm")

print(f"Image with width {image[0]} and height {image[1]}")
print(f"{image[3]}")

# write further code to test your own functions
writePGM("images/feep_copy.pgm", image)
writePGM("images/feep_inverted.pgm", invertPGM(image))
