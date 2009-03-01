
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import os

class TestCGFunction (TestCase):
    def testFunctions(self):
        values = []
        def evaluate(info, input, output):
            values.append(input)
            return input * 4
        
        self.failUnlessIsInstance(CGFunctionGetTypeID(), (int, long))

        myInfo = object()
        func = CGFunctionCreate(myInfo, 1, [0, 1], 4, [0, 1, 0, 1, 0, 1, 0, 1], evaluate)
        self.failUnlessIsInstance(func, CGFunctionRef)

        v = CGFunctionRetain(func)
        self.failUnless(v is func)
        CGFunctionRelease(func)

        
        # It is not possible to "call" a CGFunction object directly, use a 
        # shading object to check that the function is actually called.

        shading = CGShadingCreateAxial(CGColorSpaceCreateDeviceRGB(), (0, 0), (50, 50), func, True, True)
        self.failUnlessIsInstance(shading, CGShadingRef)

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
                ((0, 0), (1000, 1000)), None)
        self.failUnlessIsInstance(context, CGContextRef)
        try:
            CGContextBeginPage(context, objc.NULL)

            CGContextDrawShading(context, shading)
        finally:
            CGContextEndPage(context)
            CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

        # Drawing is done, check that the shading function is actually used
        self.failIfEqual(len(values), 0)
        for item in values:
            self.failUnlessIsInstance(item, tuple)
            self.failUnlessEqual(len(item), 1)
            self.failUnlessIsInstance(item[0], float)

        del func




        

if __name__ == "__main__":
    main()
