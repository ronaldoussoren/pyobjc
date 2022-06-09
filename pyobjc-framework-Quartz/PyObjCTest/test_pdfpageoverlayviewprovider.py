from PyObjCTools.TestSupport import TestCase
import Quartz  # noqa: F401
import objc


class TestPDFPageOverlayViewProvider(TestCase):
    def test_protocols(self):
        objc.protocolNamed("PDFPageOverlayViewProvider")
