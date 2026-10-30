from PyObjCTools.TestSupport import TestCase

import Quartz  # noqa: F401


class TestQLPreviewItem(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("QLPreviewItem", Quartz)
