from PyObjCTools.TestSupport import TestCase

import SharedWithYou  # noqa: F401


class TestSWHighlightCenter(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SWHighlightCenterDelegate")
