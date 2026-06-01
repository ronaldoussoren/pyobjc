import objc
import ctypes
import subprocess
import os
from PyObjCTools.TestSupport import TestCase

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NSObject = objc.lookUpClass("NSObject")
NSArray = objc.lookUpClass("NSArray")


class TestAllocateBuffer(TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.check_call(
            [
                "/usr/bin/xcrun",
                "swiftc",
                os.path.join(BASE, "Modules/objc/test/swiftobject.swift"),
                "-emit-library",
                "-o",
                os.path.join(BASE, "swiftobject.dylib"),
            ]
        )

        cls.lib = ctypes.CDLL(os.path.join(BASE, "swiftobject.dylib"))

    @classmethod
    def tearDownClass(cls):
        del cls.lib
        if os.path.exists(os.path.join(BASE, "swiftobject.dylib")):
            os.unlink(os.path.join(BASE, "swiftobject.dylib"))

    def test_basic(self):
        classes = [
            c for c in objc.getClassList() if c.__name__.endswith("PyObjCTestObject")
        ]
        self.assertEqual(len(classes), 1)

        cls = classes[0]

        self.assertNotIn(NSObject, cls.__mro__)

        self.assertEqual(cls.alloc().init().value(), 42)

        a = NSArray.arrayWithArray_([cls.alloc().init(), cls])
        self.assertIsInstance(a[0], cls)
        self.assertIs(a[1], cls)
