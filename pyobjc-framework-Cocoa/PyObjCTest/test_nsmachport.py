import Foundation
from PyObjCTools.TestSupport import TestCase

if hasattr(Foundation, "NSMachPort"):

    class TestNSMachPort(TestCase):
        def testAlloc(self):
            obj = Foundation.NSMachPort.alloc()
            self.assertIsNot(obj, None)

            obj = obj.init()
            self.assertIsNot(obj, None)
