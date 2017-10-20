from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import CoreSpotlight

    class TestCoreSpotlight (TestCase):
        def testConstants(self):
            self.assertIsInstance(CoreSpotlight.CoreSpotlightVersionNumber, float)
            self.assertIsInstance(CoreSpotlight.CoreSpotlightVersionString, bytes)

if __name__ == "__main__":
    main()
