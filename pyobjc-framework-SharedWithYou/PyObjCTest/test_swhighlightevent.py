from PyObjCTools.TestSupport import TestCase

import SharedWithYou  # noqa: F401


class TestSWHighlightEvent(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SWHighlightEvent")
