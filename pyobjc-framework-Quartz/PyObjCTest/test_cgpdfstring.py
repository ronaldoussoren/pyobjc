from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGPDFString(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(Quartz.CGPDFStringRef)

    def testFunctions(self):
        Quartz.CGPDFStringGetLength

        self.assertResultIsVariableSize(Quartz.CGPDFStringGetBytePtr)

        self.assertResultIsCFRetained(Quartz.CGPDFStringCopyTextString)
        self.assertResultIsCFRetained(Quartz.CGPDFStringCopyDate)
