
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import os

class TestCGLayer (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGLayerRef)

    def setUp(self):
        url = CFURLCreateWithFileSystemPath(None,
            "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
            ((0, 0), (1000, 1000)), None)
        self.failUnlessIsInstance(context, CGContextRef)
        CGContextBeginPage(context, objc.NULL)

        self.context = context

    def tearDown(self):
        CGContextEndPage(self.context)
        CGPDFContextClose(self.context)
        self.context = None
        if os.path.exists("/tmp/pyobjc.test.pdf"):
            os.unlink("/tmp/pyobjc.test.pdf")


    def testFunctions(self):
        self.failUnlessResultIsCFRetained(CGLayerCreateWithContext)
        layer = CGLayerCreateWithContext(self.context, CGSize(50, 100), None)
        self.failUnlessIsInstance(layer, CGLayerRef)

        v = CGLayerRetain(layer)
        self.failUnless(v is layer)
        CGLayerRelease(layer)

        sz = CGLayerGetSize(layer)
        self.failUnlessIsInstance(sz, CGSize)
        self.failUnlessEqual(sz, CGSize(50, 100))

        self.failIfResultIsCFRetained(CGLayerGetContext)
        ctx = CGLayerGetContext(layer)
        self.failUnlessIsInstance(ctx, CGContextRef)
        self.failIf(ctx is self.context)

        CGContextDrawLayerInRect(self.context, CGRectMake(0, 0, 50, 50), layer)
        CGContextDrawLayerAtPoint(self.context, CGPoint(10, 10), layer)

        self.failUnlessIsInstance(CGLayerGetTypeID(), (int, long))

if __name__ == "__main__":
    main()
