from PyObjCTools.TestSupport import TestCase

import Accessibility
import objc


class TestAXCustomContent(TestCase):
    def test_constants(self):
        self.assertEqual(Accessibility.AXCustomContentImportanceDefault, 0)
        self.assertEqual(Accessibility.AXCustomContentImportanceHigh, 1)

    def test_protocols(self):
        objc.protocolNamed("AXCustomContentProvider")
