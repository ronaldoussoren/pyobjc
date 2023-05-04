from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Quartz  # noqa: F401


class TestPDFPageOverlayViewProvider(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("PDFPageOverlayViewProvider")
