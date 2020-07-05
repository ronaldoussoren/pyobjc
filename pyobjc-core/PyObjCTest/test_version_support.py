import plistlib

from PyObjCTools.TestSupport import TestCase
import objc


class TestVersionSupport(TestCase):
    def test_macos_available(self):
        self.assertFalse(objc.macos_available(11, 20, 20))

        with open("/System/Library/CoreServices/SystemVersion.plist", "rb") as fp:
            if hasattr(plistlib, "load"):
                pl = plistlib.load(fp)
            else:
                pl = plistlib.readPlist(fp)

        version = (list(map(int, pl["ProductVersion"].split("."))) + [0])[:3]

        self.assertTrue(objc.macos_available(*version))
        self.assertTrue(objc.macos_available(*version[:2]))

        self.assertFalse(objc.macos_available(version[0] + 1, version[1], version[2]))
        self.assertFalse(objc.macos_available(version[0], version[1] + 1, version[2]))
        self.assertFalse(objc.macos_available(version[0], version[1], version[2] + 1))

        self.assertTrue(objc.macos_available(version[0], version[1] - 1, version[2]))
        self.assertTrue(objc.macos_available(version[0], version[1] - 1, 0))
        self.assertTrue(objc.macos_available(version[0], version[1] - 1))

        if version[2]:
            self.assertTrue(
                objc.macos_available(version[0], version[1], version[2] - 1)
            )
