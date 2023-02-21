import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestTollFreeBridging(TestCase):
    def testImplicitFromCF(self):
        c = CoreFoundation.CFArrayCreateMutable(None, 0, None)
        self.assertIsInstance(c, CoreFoundation.CFMutableArrayRef)

        nsa = Foundation.NSMutableArray.array()
        nsa.addObject_(c)

        o = nsa[0]
        self.assertIsInstance(o, Foundation.NSMutableArray)
