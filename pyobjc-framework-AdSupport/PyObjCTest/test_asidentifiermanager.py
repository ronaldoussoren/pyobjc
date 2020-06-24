from PyObjCTools.TestSupport import TestCase, min_os_level
import AdSupport


class ASIdentifierManager(TestCase):
    @min_os_level("10.14")
    def test_classes(self):
        AdSupport.ASIdentifierManager

    @min_os_level("10.14")
    def test_methods(self):
        self.assertResultIsBOOL(
            AdSupport.ASIdentifierManager.isAdvertisingTrackingEnabled
        )
