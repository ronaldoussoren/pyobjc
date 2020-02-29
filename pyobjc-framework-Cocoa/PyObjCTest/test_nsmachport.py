import Foundation
import objc
from PyObjCTools.TestSupport import *

if hasattr(Foundation, "NSMachPort"):

    class TestNSMachPort(TestCase):
        def testAlloc(self):
            obj = Foundation.NSMachPort.alloc()
            self.assertIsNot(obj, None)

            obj = obj.init()
            self.assertIsNot(obj, None)


if __name__ == "__main__":
    main()
