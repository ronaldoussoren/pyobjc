import objc
import os
import pathlib
import tempfile
from PyObjCTest.fsref import OC_TestFSRefHelper
from PyObjCTools.TestSupport import TestCase


class TestFSRef(TestCase):
    def testBasicInterface(self):
        self.assertArgIsIn(OC_TestFSRefHelper.pathForFSRef_, 0)
        self.assertArgIsOut(OC_TestFSRefHelper.getFSRef_forPath_, 0)

    def testResult(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_("/Library")
        self.assertIsInstance(ref, objc.FSRef)

        self.assertIsInstance(ref.data, bytes)
        self.assertIsInstance(ref.as_pathname(), str)

        with tempfile.NamedTemporaryFile() as fp:
            name = fp.name
            ref = o.fsrefForPath_(fp.name)

        self.assertFalse(os.path.exists(name))
        with self.assertRaisesRegex(OSError, r"MAC Error -\d+"):
            ref.as_pathname()

    def testArg(self):
        # return  #
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_("/Library")
        self.assertIsInstance(ref, objc.FSRef)

        p = o.stringForFSRef_(ref)
        self.assertIsInstance(p, str)
        self.assertEqual(p, "/Library")

        with self.assertRaisesRegex(ValueError, "Cannot convert value to FSRef"):
            o.stringForFSRef_("/etc/hosts")

    def testInput(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_("/Library")
        self.assertIsInstance(ref, objc.FSRef)

        p = o.pathForFSRef_(ref)
        self.assertIsInstance(p, str)
        self.assertEqual(p, "/Library")

    def testOutput(self):
        return  # XX
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.getFSRef_forPath_(None, "/Library")
        self.assertIsInstance(ref, objc.FSRef)

        # Verify the fsref contents:
        p = o.stringForFSRef_(ref)
        self.assertIsInstance(p, str)
        self.assertEqual(p, "/Library")

    def test_frompath(self):
        ref = objc.FSRef.from_pathname("/etc/hosts")
        self.assertIsInstance(ref, objc.FSRef)

        self.assertEqual(ref.as_pathname(), os.path.realpath("/etc/hosts"))

        ref = objc.FSRef.from_pathname(b"/etc/hosts")
        self.assertIsInstance(ref, objc.FSRef)

        self.assertEqual(ref.as_pathname(), os.path.realpath("/etc/hosts"))

        ref = objc.FSRef.from_pathname(pathlib.Path("/etc/hosts"))
        self.assertIsInstance(ref, objc.FSRef)

        self.assertEqual(ref.as_pathname(), os.path.realpath("/etc/hosts"))

        with self.assertRaisesRegex(
            TypeError, "expected str, bytes or os.PathLike object, not int"
        ):
            objc.FSRef.from_pathname(42)

        with self.assertRaisesRegex(UnicodeEncodeError, r".*surrogates not allowed"):
            objc.FSRef.from_pathname("\uDC00")

        with self.assertRaisesRegex(OSError, r"MAC Error -\d+"):
            objc.FSRef.from_pathname("no-such-file.missing")

        with self.assertRaisesRegex(
            TypeError, "expected str, bytes or os.PathLike object, not int"
        ):
            objc.FSRef.from_pathname(42)

    def test_sizeof(self):
        ref = objc.FSRef.from_pathname("/etc/hosts")
        self.assertIsInstance(ref.__sizeof__(), int)

    def test_as_bytes(self):
        ref = objc.FSRef.from_pathname("/etc/hosts")
        self.assertIsInstance(ref.data, bytes)

        # XXX: there's not really much we can do here...
