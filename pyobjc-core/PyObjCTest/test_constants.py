import objc
import platform
from PyObjCTools.TestSupport import TestCase


class TestConstants(TestCase):
    def test_version_current(self):
        self.assertIsInstance(objc.MAC_OS_X_VERSION_CURRENT, int)

        # Use platform.mac_ver() to calculate the expected value,
        # that matches the version seen by ObjC code. The test
        # function os_release() returns the actual system version.
        # The two will be different when running on macOS 11 or later
        # with a binary compiled using the 10.15 SDK (or earlier).

        # v = os_release().split(".")[:2]
        v = platform.mac_ver()[0].split(".")[:2]
        v = "MAC_OS_X_VERSION_%s_%s" % tuple(v)

        self.assertGreaterEqual(objc.MAC_OS_X_VERSION_CURRENT, getattr(objc, v))

    def test_version_values(self):
        self.assertEqual(objc.MAC_OS_X_VERSION_10_0, 1000)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_1, 1010)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_2, 1020)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_3, 1030)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_4, 1040)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_5, 1050)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_6, 1060)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_7, 1070)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_8, 1080)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_9, 1090)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_10, 101_000)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_10_2, 101_002)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_10_3, 101_003)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_11, 101_100)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_11_2, 101_102)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_11_3, 101_103)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_11_4, 101_104)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_12, 101_200)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_12_1, 101_201)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_12_2, 101_202)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_12_4, 101_204)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13, 101_300)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_1, 101_301)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_2, 101_302)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_4, 101_304)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_5, 101_305)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_6, 101_306)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_14, 101_400)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_14_1, 101_401)
