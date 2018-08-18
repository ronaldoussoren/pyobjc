from PyObjCTools.TestSupport import *
import objc

class TestConstants (TestCase):
    def test_version_current(self):
        self.assertIsInstance(objc.MAC_OS_X_VERSION_CURRENT, (int, long))

        v = os_release().split('.')[:2]
        v = 'MAC_OS_X_VERSION_%s_%s'%tuple(v)

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
        self.assertEqual(objc.MAC_OS_X_VERSION_10_10, 101000)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_10_2, 101002)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_10_3, 101003)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_11, 101100)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_11_2, 101102)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_11_3, 101103)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_11_4, 101104)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_12, 101200)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_12_1, 101201)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_12_2, 101202)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_12_4, 101204)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13, 101300)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_1, 101301)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_2, 101302)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_4, 101304)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_5, 101305)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_13_6, 101306)
        self.assertEqual(objc.MAC_OS_X_VERSION_10_14, 101400)

if __name__ == "__main__":
    main()
