"""
Some tests for difficult wrapped graphics functions and methods

NOTE: These require a WindowServer connection on MacOS X
"""
import unittest
from AppKit import *
from Foundation import *
import array
import sys


class SimpleImage:
    """
    Helper class that makes it easier to access individual pixels in
    a bitmap image
    """
    def __init__(self, image):
        data = image.TIFFRepresentation()
        bitmap = NSBitmapImageRep.imageRepWithData_(data)
        self.bitmap = bitmap
        self.data = bitmap.bitmapData()
        self.rowbytes = bitmap.bytesPerRow()
        self.pixbytes = bitmap.bitsPerPixel() / 8
        self.rowCount = bitmap.pixelsHigh()

        if bitmap.isPlanar():
            raise ValueError, "Planar image!"
        if (bitmap.bitsPerPixel() % 8) != 0:
            raise ValueError, "bits per pixel isn't multiple of 8"

    def width(self):
        return self.bitmap.pixelsWide()

    def height(self):
        return self.bitmap.pixelsHigh()

    def getPixel(self, x, y):
        x = self.rowCount - 1 - x
        rowOffset = x * self.rowbytes
        pixelOffset = y * self.pixbytes
        offset = rowOffset + pixelOffset

        pixel = self.data[offset:offset + self.pixbytes]
        return pixel

class RectTest (unittest.TestCase):
    def setUp(self):

        # Force NSApp initialisation, needed for some of the tests
        NSApplication.sharedApplication().activateIgnoringOtherApps_(0)



        self.points = (
            ((10,  0), ( 1,  1)),
            ((10, 10), ( 1,  1)),
            (( 0, 10), ( 1,  1)),
            (( 0,  0), ( 1,  1)),
            ((70, 70), (10, 10))
        )

        self.image = NSImage.alloc().initWithSize_((100, 100))

    def makeArray(self, points):

        a = array.array('f', len(points) * [0, 0, 0, 0])
        for i in range(len(points)):
            p = points[i]
            a[(i*4) + 0] = p[0][0]
            a[(i*4) + 1] = p[0][1]
            a[(i*4) + 2] = p[1][0]
            a[(i*4) + 3] = p[1][1]

        return a

    def assertImagePoints(self, image, points):
        """
        Check that the image contains white pixels everywhere but at the
        specified locations points is sequence of NSRect values.
        """

        img = SimpleImage(image)

        allpoints = [ (x, y)
                for x in range(img.width())
                for y in range(img.height())
        ]

        # Check black points
        for ((x, y), (h, w)) in points:
            for ox in range(w):
                for oy in range(h):
                    allpoints.remove((x+ox, y+oy))
                    self.assertEquals(
                        img.getPixel(x+ox, y+oy),
                        '\x00\x00\x00\xff',
                        'Black pixel at %d,%d'%(x+ox, y+oy))

        # And white points
        for x, y in allpoints:
            self.assertEquals(
                img.getPixel(x, y),
                '\x00\x00\x00\x00',
                'White pixel at %d,%d'%(x, y))


    def tearDown(self):
        pass


    def test_NSRectFillList_tuple(self):
        """
        Check NSRectFillList with a tuple of NSRects
        """
        self.image.lockFocus()
        NSRectFillList(self.points, len(self.points))
        self.image.unlockFocus()

        self.assertImagePoints(self.image, self.points)

    def test_NSRectFillList_array(self):
        """
        Check NSRectFillList with a array.array of NSRects
        """
        self.image.lockFocus()
        NSRectFillList(self.makeArray(self.points), len(self.points))
        self.image.unlockFocus()


if __name__ == "__main__":
    unittest.main()
