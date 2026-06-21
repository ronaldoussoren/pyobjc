from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCGPDFDictionary(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(Quartz.CGPDFDictionaryRef)

    def assertIsPDFGetter(self, function):
        self.assertArgIsIn(function, 1)
        self.assertArgIsNullTerminated(function, 1)
        self.assertArgIsOut(function, 2)

    def testIncomplete(self):
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetObject)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetBoolean)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetInteger)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetNumber)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetName)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetString)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetArray)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetDictionary)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetStream)

        # self.assertArgIsFunction(CGPDFDictionaryApplyFunction, 1, b"vn^t^{CGPDFObject=}^v", False)
        self.assertFalse(isinstance(Quartz.CGPDFDictionaryApplyFunction, objc.function))

    def test_functions(self):
        Quartz.CGPDFDictionaryGetCount

    @min_os_level("10.14")
    def test_functions10_14(self):
        self.assertArgIsBlock(
            Quartz.CGPDFDictionaryApplyBlock, 1, b"vn^t^{CGPDFObject=}^v"
        )
