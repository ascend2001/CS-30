import struct
from functools import reduce
from collections import namedtuple

pixel = namedtuple("pixel", "r g b")

'''
You need to implement the six functions defined below.
Each function takes a single argument:
  an image represented as a list of lists of pixels, where
  each pixel has the type pixel defined above.
Each function returns a list in exactly that same form.

The readPPM and writePPM functions defined at the end of the file should NOT be
called by your code.  Rather, they are provided to help you test your code:
readPPM allows you to convert PPM image files into lists of lists of pixels that
can be passed as arguments to your functions, and writePPM allows you to write the
results of your functions to image files so that the images can be viewed.
'''
def negate(pixels):
    return list(map(lambda n:list(map(lambda m:pixel(r=255-m.r,g=255-m.g,b=255-m.b),n)),pixels))

def test_negate():
    assert(negate([[pixel(0,255,34),pixel(255,255,255)],[pixel(0,0,0),pixel(125,200,35)]])==[[pixel(255,0,221),pixel(0,0,0)],[pixel(255,255,255),pixel(130,55,220)]])
    assert(negate([[pixel(90,45,199),pixel(56,99,134)],[pixel(45,254,98),pixel(244,0,12)]])==[[pixel(165,210,56),pixel(199,156,121)],[pixel(210,1,157),pixel(11,255,243)]])
    assert(negate(readPPM("example.ppm"))==[[pixel(r=245, g=232, b=203), pixel(r=173, g=252, b=40)], [pixel(r=225, g=74, b=154), pixel(r=222, g=210, b=50)], [pixel(r=215, g=187, b=163), pixel(r=144, g=179, b=254)]])


def greyscale(pixels):
    return list(map(lambda n:(list(map(lambda m:pixel(r=int(round(0.299*m.r+0.587*m.g+0.114*m.b)),g=int(round(0.299*m.r+0.587*m.g+0.114*m.b)),b=int(round(0.299*m.r+0.587*m.g+0.114*m.b))),n))),pixels))

def test_greyscale():
    assert(greyscale(readPPM("example.ppm"))==[[pixel(22, 22, 22), pixel(51, 51, 51)], [pixel(127, 127, 127), pixel(60, 60, 60)],[pixel(62, 62, 62), pixel(78, 78, 78)]])
    assert(greyscale([[pixel(255,255,255),pixel(255,0,255)],[pixel(23,34,45),pixel(123,234,100)]])==[[pixel(255,255,255),pixel(105,105,105)],[pixel(32,32,32),pixel(186,186,186)]])


def upsideDown(pixels):
    return pixels[::-1]

def test_upsideDown():
    assert(upsideDown([[pixel(12,98,47),pixel(255,0,255)],[pixel(109,256,25),pixel(55,44,0)]])==[[pixel(109,256,25),pixel(55,44,0)],[pixel(12,98,47),pixel(255,0,255)]])
    assert(upsideDown([[pixel(0,255,34),pixel(255,255,255)],[pixel(0,0,0),pixel(125,200,35)]])==[[pixel(0,0,0),pixel(125,200,35)],[pixel(0,255,34),pixel(255,255,255)]])
    assert(upsideDown([[pixel(0,255,34),pixel(255,255,255)],[pixel(0,0,0),pixel(125,200,35)]])==[[pixel(0,0,0),pixel(125,200,35)],[pixel(0,255,34),pixel(255,255,255)]])


def mirrorImage(pixels):
    return list(map(lambda n: n[::-1],pixels))


def compress(pixels):
    a=list(map(lambda n:n[::2],pixels))
    return a[::2]


def decompress(pixels):
    def duplicate(l):
        if l==[]:
            return []
        else:
            head=l[0]
            tail=l[1:]
            return 2*[head]+duplicate(tail)
    return duplicate(list(map(lambda n:duplicate(list(map(lambda m:m,n))),pixels)))


# read the PPM image file named fname and convert it to a list of lists of pixels.
# each pixel is an RGB triple, represented using the type pixel defined above.
# each list of pixels represents one row in the image, ordered from top to bottom.
def readPPM(fname):
    f = open(fname, "rb")
    p6Ignore = f.readline()
    dimensions = f.readline().split()
    width = int(dimensions[0])
    height = int(dimensions[1])
    maxIgnore = f.readline()

    pixels = []
    rgbData = [x for x in f.read()]
    f.close()
    for r in range(height):
        row = []
        for c in range(width):
            i = 3 * (r * width + c)
            row.append(pixel(r=rgbData[i], g=rgbData[i+1], b=rgbData[i+2]))
        pixels.append(row)
    return pixels

floImage=readPPM("florence.ppm")

# pixels should be a list of list of RGB triples, in the same format as returned
# by the readPPM function above.
# this function writes those pixels to the file named fname as a PPM image.
def writePPM(pixels, fname):
    f = open(fname, "wb")
    f.write("P6\n".encode())
    width = len(pixels[0])
    height = len(pixels)
    f.write((str(width) + " " + str(height) + "\n").encode())
    f.write((str(255) + "\n").encode())
    bPixels = [[struct.pack('BBB', p.r, p.g, p.b) for p in r] for r in pixels]
    flatPixels = reduce(lambda x,y: x+y, bPixels)
    f.writelines(flatPixels)
    f.close()
