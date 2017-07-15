from PyObjCTools.TestSupport import *

import CoreSpotlight

class TestCoreSpotlight (TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreSpotlight.CoreSpotlightVersionNumber, float)
        self.assertIsInstance(CoreSpotlight.CoreSpotlightVersionString, bytes)

if __name__ == "__main__":
    main()
