import sys

import objc
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import ExternalAccessory

    class TestEAWiFiUnconfiguredAccessory(TestCase):
        def testConstants(self):
            self.assertEqual(
                ExternalAccessory.EAWiFiUnconfiguredAccessoryPropertySupportsAirPlay,
                1 << 0,
            )
            self.assertEqual(
                ExternalAccessory.EAWiFiUnconfiguredAccessoryPropertySupportsAirPrint,
                1 << 1,
            )
            self.assertEqual(
                ExternalAccessory.EAWiFiUnconfiguredAccessoryPropertySupportsHomeKit,
                1 << 2,
            )


if __name__ == "__main__":
    main()
