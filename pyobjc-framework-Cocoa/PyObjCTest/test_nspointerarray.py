import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSPointerArray(TestCase):
    def testPointers(self):
        o = Foundation.NSPointerArray.pointerArrayWithStrongObjects()

        m = o.addPointer_.__metadata__()
        self.assertEqual(m["arguments"][2]["type"], b"@")

        m = o.insertPointer_atIndex_.__metadata__()
        self.assertEqual(m["arguments"][2]["type"], b"@")

        m = o.replacePointerAtIndex_withPointer_.__metadata__()
        self.assertEqual(m["arguments"][3]["type"], b"@")

        m = o.pointerAtIndex_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"@")
