import Foundation
from PyObjCTools.TestSupport import TestCase

if hasattr(Foundation, "NSMachPort"):

    class TestNSMachPort(TestCase):
        def test_alloc(self):
            obj = Foundation.NSMachPort.alloc()
            self.assertIsNot(obj, None)

            obj = obj.init()
            self.assertIsNot(obj, None)
