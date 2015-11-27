from PyObjCTools.TestSupport import *

import AppKit


class TestNSTextAlternatives (TestCase):
    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(AppKit.NSTextAlternativesSelectedAlternativeStringNotification, unicode)

if __name__ == "__main__":
    main()
