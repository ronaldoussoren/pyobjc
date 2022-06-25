from PyObjCTools.TestSupport import TestCase
import Quartz  # noqa: F401


class TestPDFPageOverlayViewProvider(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("PDFPageOverlayViewProvider")
