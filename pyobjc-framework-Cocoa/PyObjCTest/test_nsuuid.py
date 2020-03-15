import uuid

import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSUUID(TestCase):
    @min_os_level("10.8")
    def testMethods10_8(self):
        val = Foundation.NSUUID.UUID()

        self.assertArgIsOut(val.getUUIDBytes_, 0)
        self.assertArgIsIn(val.initWithUUIDBytes_, 0)

        v = val.getUUIDBytes_(None)
        self.assertIsInstance(v, bytes)
        self.assertEqual(len(v), 16)

        w = uuid.UUID(bytes=v)

        self.assertEqual(str(w).lower(), val.UUIDString().lower())

        w = uuid.uuid1()
        val = Foundation.NSUUID.alloc().initWithUUIDBytes_(w.bytes)
        self.assertEqual(str(w).lower(), val.UUIDString().lower())
