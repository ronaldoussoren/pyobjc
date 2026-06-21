from PyObjCTools.TestSupport import TestCase, min_sdk_level
import CoreML


class TestMLWritableHelper(CoreML.NSObject):
    def writeToURL_error_(self, a, b):
        pass


class TestMLWritable(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists("MLWritable", CoreML)

    def test_methods(self):
        self.assertResultIsBOOL(TestMLWritableHelper.writeToURL_error_)
        self.assertArgHasType(TestMLWritableHelper.writeToURL_error_, 1, b"o^@")
