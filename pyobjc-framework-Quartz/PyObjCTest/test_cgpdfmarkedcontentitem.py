from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGPDFMarkedContentItem(TestCase):
    @min_os_level("27.0")
    def test_types(self):
        self.assertIsCFType(Quartz.CGPDFMarkedContentItemRef, unique=False)

    @min_os_level("27.0")
    def test_functions(self):
        Quartz.CGPDFMarkedContentItemRetain
        Quartz.CGPDFMarkedContentItemRelease
