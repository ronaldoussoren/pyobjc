from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGSession(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGSessionUserIDKey, "kCGSSessionUserIDKey")
        self.assertEqual(Quartz.kCGSessionUserNameKey, "kCGSSessionUserNameKey")
        self.assertEqual(Quartz.kCGSessionConsoleSetKey, "kCGSSessionConsoleSetKey")
        self.assertEqual(Quartz.kCGSessionOnConsoleKey, "kCGSSessionOnConsoleKey")
        self.assertEqual(Quartz.kCGSessionLoginDoneKey, "kCGSessionLoginDoneKey")
        self.assertEqual(
            Quartz.kCGNotifyGUIConsoleSessionChanged,
            b"com.apple.coregraphics.GUIConsoleSessionChanged",
        )
        self.assertEqual(
            Quartz.kCGNotifyGUISessionUserChanged,
            b"com.apple.coregraphics.GUISessionUserChanged",
        )

    def testFunctions(self):
        v = Quartz.CGSessionCopyCurrentDictionary()
        self.assertIsInstance(v, Quartz.CFDictionaryRef)

        self.assertIsInstance(v[Quartz.kCGSessionUserIDKey], int)
        self.assertIsInstance(v[Quartz.kCGSessionUserNameKey], str)
        # self.assertIsInstance(v[Quartz.kCGSessionConsoleSetKey], int)
        # self.assertIsInstance(v[Quartz.kCGSessionOnConsoleKey], bool)
        # self.assertIsInstance(v[Quartz.kCGSessionLoginDoneKey], bool)
