# Python code to convert an image to ASCII image.
import sys
import random
import argparse
import numpy as np
import math

from PIL import Image

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def getAverageL(array, startx, starty, w, h):
    """
    Given NumPy Array of Image, return average value of grayscale value
    """
    avg = 0
    for xoffset in range(w):
        for yoffset in range(h):
            avg += array[starty + yoffset][startx + xoffset]
    avg //= w * h
    return avg


def covertImageToAscii(fileName, cols, scale) -> Image:
    """
    Given Image and dims (rows, cols) returns an m*n list of Images
    """
    global gscale1

    # open image and convert to grayscale
    image = Image.open(fileName).convert('L')
    imagearray = np.array(image)

    # store dimensions
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))

    # compute width of tile
    w = W/cols

    # compute tile height based on aspect ratio and scale
    h = w/scale

    # compute number of rows
    rows = int(H/h)

    print("cols: %d, rows: %d" % (cols, h))
    print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        aimg.append("")

        for i in range(cols):
            x1 = int(i*w)

            # get average luminance
            avg = int(getAverageL(imagearray, x1, y1, int(w), int(h)))

            # look up ascii char
            gsval = gscale1[-int((avg*69)/255)]

            # append ascii char to string
            aimg[j] += gsval
    # return txt image
    return aimg


def main():
    # create parser
    descStr = "This program converts an image into ASCII art."
    # set output file
    outFile = 'out.txt'

    # set scale default as 0.43 which suits
    # a Courier font
    scale = 0.43
    # set cols
    cols = 1920

    print('generating ASCII art...')
    # convert image to ascii txt
    aimg = covertImageToAscii("example.jpg", cols, scale)
    # open file
    f = open(outFile, 'w')

    # write to file
    for row in aimg:
        f.write(row + '\n')

    # cleanup
    f.close()
    print("ASCII art written to %s" % outFile)


# call main
if __name__ == '__main__':
    main()
