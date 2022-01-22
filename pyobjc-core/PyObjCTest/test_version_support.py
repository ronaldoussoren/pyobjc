import plistlib

from PyObjCTools.TestSupport import TestCase
import objc


class TestVersionSupport(TestCase):
    def test_macos_available(self):
        self.assertFalse(objc.macos_available(99, 20, 20))

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
        self.assertTrue(objc.macos_available(9, 0))

        if version[2]:
            self.assertTrue(
                objc.macos_available(version[0], version[1], version[2] - 1)
            )

        with self.assertRaisesRegex(
            TypeError,
            r"(function missing required argument 'major' \(pos 1\))|(Required argument 'major' \(pos 1\) not found)",
        ):
            objc.macos_available()

        with self.assertRaisesRegex(
            TypeError,
            r"('str' object cannot be interpreted as an integer)|(an integer is required \(got type str\))",
        ):
            objc.macos_available("42", 0)
