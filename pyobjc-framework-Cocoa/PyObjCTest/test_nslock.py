import Foundation
import objc

import unittest


class TestNSLockProtocols (unittest.TestCase):

    def testLockIsLock(self):
        # Test for bug #1735937
        lock = Foundation.NSLock.alloc().init()
        self.assert_(lock.conformsToProtocol_(objc.protocolNamed("NSLocking")))

        self.assert_(lock.conformsToProtocol_(Foundation.protocols.NSLocking))

if __name__ == "__main__":
    unittest.main()
