from PyObjCTools.TestSupport import TestCase

import SharedWithYou  # noqa: F401
import objc


class TestSWHighlightCenter(TestCase):
    def test_protocols(self):
        objc.protocolNamed("SWHighlightCenterDelegate")
