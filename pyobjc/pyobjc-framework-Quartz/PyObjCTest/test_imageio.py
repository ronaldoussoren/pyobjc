'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
from Quartz import ImageIO

class TestImageIO (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(ImageIO, 'CGImageSourceRef') )
        self.assert_( issubclass(ImageIO.CGImageSourceRef, objc.lookUpClass('NSCFType')) )
        self.assert_( ImageIO.CGImageSourceRef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        self.assert_( hasattr(ImageIO, 'kCGImageStatusUnexpectedEOF') )
        self.assert_( isinstance(ImageIO.kCGImageStatusUnexpectedEOF, (int, long)) )
        self.assertEquals(ImageIO.kCGImageStatusUnexpectedEOF, -5)

    def testVariables(self):
        self.assert_( hasattr(ImageIO, 'kCGImageSourceTypeIdentifierHint') )
        self.assert_( isinstance(ImageIO.kCGImageSourceTypeIdentifierHint, unicode) )
        self.assert_( hasattr(ImageIO, 'kCGImagePropertyPNGDictionary') )
        self.assert_( isinstance(ImageIO.kCGImagePropertyPNGDictionary, unicode) )

    def testFunctions(self):
        self.assert_( hasattr(ImageIO, 'CGImageSourceCopyTypeIdentifiers') )
        self.assert_( hasattr(ImageIO, 'CGImageSourceCreateIncremental') )
        self.assert_( hasattr(ImageIO, 'CGImageDestinationCreateWithDataConsumer') )



if __name__ == "__main__":
    unittest.main()

