
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGSession (TestCase):

    def testConstants(self):
        self.assertEqual(kCGSessionUserIDKey, "kCGSSessionUserIDKey")
        self.assertEqual(kCGSessionUserNameKey, "kCGSSessionUserNameKey")
        self.assertEqual(kCGSessionConsoleSetKey, "kCGSSessionConsoleSetKey")
        self.assertEqual(kCGSessionOnConsoleKey, "kCGSSessionOnConsoleKey")
        self.assertEqual(kCGSessionLoginDoneKey, "kCGSessionLoginDoneKey")
        self.assertEqual(kCGNotifyGUIConsoleSessionChanged, b"com.apple.coregraphics.GUIConsoleSessionChanged")
        self.assertEqual(kCGNotifyGUISessionUserChanged, b"com.apple.coregraphics.GUISessionUserChanged")

    def testFunctions(self):
        v = CGSessionCopyCurrentDictionary()
        self.assertIsInstance(v, CFDictionaryRef)

        self.assertIsInstance(v[kCGSessionUserIDKey], (int, long))
        self.assertIsInstance(v[kCGSessionUserNameKey], unicode)
        self.assertIsInstance(v[kCGSessionConsoleSetKey], (int, long))
        self.assertIsInstance(v[kCGSessionOnConsoleKey], bool)
        self.assertIsInstance(v[kCGSessionLoginDoneKey], bool)



if __name__ == "__main__":
    main()
