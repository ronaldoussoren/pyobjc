import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import Quartz  # noqa: F401


class TestQLPreviewItem(TestCase):
    @min_os_level("10.6")
    def testClasses(self):
        v = objc.protocolNamed("QLPreviewItem")
        self.assertIsInstance(v, objc.formal_protocol)
