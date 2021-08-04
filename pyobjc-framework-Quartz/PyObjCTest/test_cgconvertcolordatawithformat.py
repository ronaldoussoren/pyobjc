from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGConvertColorDataWithFormat(TestCase):
    def testStruct(self):
        v = Quartz.CGColorDataFormat()
        self.assertIsInstance(v.version, int)
        self.assertIs(v.colorspace_info, None)
        self.assertIsInstance(v.bitmap_info, int)
        self.assertIsInstance(v.bits_per_component, int)
        self.assertIsInstance(v.bytes_per_row, int)
        self.assertIsInstance(v.intent, int)
        self.assertIs(v.decode, None)

    @min_os_level("12.0")
    def testFunctions(self):
        self.assertArgIsOut(Quartz.CGConvertColorDataWithFormat, 2)
        self.assertArgIsVariableSize(Quartz.CGConvertColorDataWithFormat, 2)
        self.assertArgIsIn(Quartz.CGConvertColorDataWithFormat, 4)
        self.assertArgIsVariableSize(Quartz.CGConvertColorDataWithFormat, 4)
