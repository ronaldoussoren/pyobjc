import os

import Quartz
from PyObjCTools.TestSupport import TestCase

import objc


class TestCGLayer(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGLayerRef)

    def setUp(self):
        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, Quartz.CFURLRef)
        context = Quartz.CGPDFContextCreateWithURL(url, ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, Quartz.CGContextRef)
        Quartz.CGContextBeginPage(context, objc.NULL)

        self.context = context

    def tearDown(self):
        Quartz.CGContextEndPage(self.context)
        if hasattr(Quartz, "CGPDFContextClose"):
            Quartz.CGPDFContextClose(self.context)
        self.context = None
        if os.path.exists("/tmp/pyobjc.test.pdf"):
            os.unlink("/tmp/pyobjc.test.pdf")

    def testFunctions(self):
        self.assertResultIsCFRetained(Quartz.CGLayerCreateWithContext)
        layer = Quartz.CGLayerCreateWithContext(
            self.context, Quartz.CGSize(50, 100), None
        )
        self.assertIsInstance(layer, Quartz.CGLayerRef)

        v = Quartz.CGLayerRetain(layer)
        self.assertTrue(v is layer)
        Quartz.CGLayerRelease(layer)

        sz = Quartz.CGLayerGetSize(layer)
        self.assertIsInstance(sz, Quartz.CGSize)
        self.assertEqual(sz, Quartz.CGSize(50, 100))

        self.assertResultIsNotCFRetained(Quartz.CGLayerGetContext)
        ctx = Quartz.CGLayerGetContext(layer)
        self.assertIsInstance(ctx, Quartz.CGContextRef)
        self.assertIsNot(ctx, self.context)

        Quartz.CGContextDrawLayerInRect(
            self.context, Quartz.CGRectMake(0, 0, 50, 50), layer
        )
        Quartz.CGContextDrawLayerAtPoint(self.context, Quartz.CGPoint(10, 10), layer)

        self.assertIsInstance(Quartz.CGLayerGetTypeID(), int)
