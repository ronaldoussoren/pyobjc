from PyObjCTools.TestSupport import *

import objc

class TestFramework (TestCase):
    def test_normal_lib(self):
        self.assertIsNone(objc.infoForFramework("/usr/lib/libSystem.dylib"))
        self.assertIsNone(objc.infoForFramework("/usr/lib/libSystem.B.dylib"))
        self.assertIsNone(objc.infoForFramework("/usr/lib/libSystem_debug.dylib"))
        self.assertIsNone(objc.infoForFramework("/usr/lib/libSystem.B_debug.dylib"))

    def test_basic_framework(self):
        self.assertEqual(("/Library/Frameworks", "Python", "Current"),
                objc.infoForFramework("/Library/Frameworks/Python.framework/Versions/Current/Python"))
        self.assertEqual(("/Library/Frameworks", "Python", "2.7"),
                objc.infoForFramework("/Library/Frameworks/Python.framework/Versions/2.7/Python"))
        self.assertEqual(("/System/Library/Frameworks", "Python", ""),
                objc.infoForFramework("/System/Library/Frameworks/Python.framework/Python"))

    def test_altname_framework(self):
        self.assertEqual(None,
                objc.infoForFramework("/Library/Frameworks/Python.framework/Versions/Current/Python_Debug"))
        self.assertEqual(None,
                objc.infoForFramework("/Library/Frameworks/Python.framework/Versions/2.7/Python_Debug"))
        self.assertEqual(None,
                objc.infoForFramework("/Library/Frameworks/Python.framework/Python_Debug"))

    def test_nested_framework(self):
        self.assertEqual(("/System/Library/Frameworks/CoreServices.framework/Frameworks", "AE", "A"),
                objc.infoForFramework(
                    "/System/Library/Frameworks/CoreServices.framework/Frameworks/AE.framework/Versions/A/AE"))

        self.assertEqual(("/System/Library/Frameworks/CoreServices.framework/Frameworks", "AE", ""),
                objc.infoForFramework(
                    "/System/Library/Frameworks/CoreServices.framework/Frameworks/AE.framework/AE"))

        self.assertEqual(("/System/Library/Frameworks/CoreServices.framework/Versions/B/Frameworks", "AE", "A"),
                objc.infoForFramework(
                    "/System/Library/Frameworks/CoreServices.framework/Versions/B/Frameworks/AE.framework/Versions/A/AE"))



if __name__ == "__main__":
    main()
