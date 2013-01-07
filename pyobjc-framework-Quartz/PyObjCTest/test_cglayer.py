
from PyObjCTools.TestSupport import *
from Quartz import *
import Quartz
import os

try:
    long
except NameError:
    long = int

class TestCGLayer (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGLayerRef)

    def setUp(self):
        url = CFURLCreateWithFileSystemPath(None,
            "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
            ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, CGContextRef)
        CGContextBeginPage(context, objc.NULL)

        self.context = context

    def tearDown(self):
        CGContextEndPage(self.context)
        if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(self.context)
        self.context = None
        if os.path.exists("/tmp/pyobjc.test.pdf"):
            os.unlink("/tmp/pyobjc.test.pdf")


    def testFunctions(self):
        self.assertResultIsCFRetained(CGLayerCreateWithContext)
        layer = CGLayerCreateWithContext(self.context, CGSize(50, 100), None)
        self.assertIsInstance(layer, CGLayerRef)

        v = CGLayerRetain(layer)
        self.assertTrue(v is layer)
        CGLayerRelease(layer)

        sz = CGLayerGetSize(layer)
        self.assertIsInstance(sz, CGSize)
        self.assertEqual(sz, CGSize(50, 100))

        self.assertResultIsNotCFRetained(CGLayerGetContext)
        ctx = CGLayerGetContext(layer)
        self.assertIsInstance(ctx, CGContextRef)
        self.assertIsNot(ctx, self.context)

        CGContextDrawLayerInRect(self.context, CGRectMake(0, 0, 50, 50), layer)
        CGContextDrawLayerAtPoint(self.context, CGPoint(10, 10), layer)

        self.assertIsInstance(CGLayerGetTypeID(), (int, long))

if __name__ == "__main__":
    main()
