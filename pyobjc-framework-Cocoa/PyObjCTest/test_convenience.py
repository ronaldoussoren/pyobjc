import struct
import sys

from PyObjCTools.TestSupport import TestCase
import objc

NSObject = objc.lookUpClass("NSObject")


class OC_TestConveniences(NSObject):
    def initWithHashValue_(self, hashValue):
        self = objc.super(OC_TestConveniences, self).init()
        self.hashValue = hashValue
        return self

    def hash(self):  # noqa: A003
        return self.hashValue


class TestConveniences(TestCase):
    def testHash(self):
        for hashValue in (0, sys.maxsize, sys.maxsize + 1, 0xFFFFFFFF):
            expect = struct.unpack("l", struct.pack("L", hashValue))[0]
            # Python can't hash to -1.  Surprise! :)
            if expect == -1:
                expect = -2
            o = OC_TestConveniences.alloc().initWithHashValue_(hashValue)
            self.assertEqual(o.hash(), hashValue)
            self.assertEqual(
                hash(o),
                expect,
                f"o.hash() == 0x{o.hash():X} | {hash(o)!r} != {expect!r}",
            )
