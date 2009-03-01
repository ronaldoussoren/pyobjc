
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGSession (TestCase):

    def testConstants(self):
        self.failUnlessEqual(kCGSessionUserIDKey, "kCGSSessionUserIDKey")
        self.failUnlessEqual(kCGSessionUserNameKey, "kCGSSessionUserNameKey")
        self.failUnlessEqual(kCGSessionConsoleSetKey, "kCGSSessionConsoleSetKey")
        self.failUnlessEqual(kCGSessionOnConsoleKey, "kCGSSessionOnConsoleKey")
        self.failUnlessEqual(kCGSessionLoginDoneKey, "kCGSessionLoginDoneKey")
        self.failUnlessEqual(kCGNotifyGUIConsoleSessionChanged, "com.apple.coregraphics.GUIConsoleSessionChanged")
        self.failUnlessEqual(kCGNotifyGUISessionUserChanged, "com.apple.coregraphics.GUISessionUserChanged")

    def testFunctions(self):
        v = CGSessionCopyCurrentDictionary()
        self.failUnlessIsInstance(v, CFDictionaryRef)

        self.failUnlessIsInstance(v[kCGSessionUserIDKey], (int, long))
        self.failUnlessIsInstance(v[kCGSessionUserNameKey], unicode)
        self.failUnlessIsInstance(v[kCGSessionConsoleSetKey], (int, long))
        self.failUnlessIsInstance(v[kCGSessionOnConsoleKey], bool)
        self.failUnlessIsInstance(v[kCGSessionLoginDoneKey], bool)



if __name__ == "__main__":
    main()
