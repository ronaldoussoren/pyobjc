import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINPersonHandleLabel (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertIsInstance(Intents.INPersonHandleLabelHome, unicode)
            self.assertIsInstance(Intents.INPersonHandleLabelWork, unicode)
            self.assertIsInstance(Intents.INPersonHandleLabeliPhone, unicode)
            self.assertIsInstance(Intents.INPersonHandleLabelMobile, unicode)
            self.assertIsInstance(Intents.INPersonHandleLabelMain, unicode)
            self.assertIsInstance(Intents.INPersonHandleLabelHomeFax, unicode)
            self.assertIsInstance(Intents.INPersonHandleLabelWorkFax , unicode)
            self.assertIsInstance(Intents.INPersonHandleLabelPager, unicode)
            self.assertIsInstance(Intents.INPersonHandleLabelOther, unicode)


if __name__ == "__main__":
    main()
