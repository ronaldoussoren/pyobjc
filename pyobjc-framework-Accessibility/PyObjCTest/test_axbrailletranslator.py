from PyObjCTools.TestSupport import TestCase, min_os_level

import Accessibility


class TestAXBrailleTranslator(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(Accessibility.AXBrailleTable.isEightDot)
