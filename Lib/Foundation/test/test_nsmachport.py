import unittest
import objc

from Foundation import NSMachPort

class TestNSMachPort(unittest.TestCase):
    def testAlloc(self):
        obj = NSMachPort.alloc()
        self.assert_(obj is not None)

        obj = obj.init()
        self.assert_(obj is not None)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNSMachPort))
    return suite

if __name__ == '__main__':
    unittest.main( )
