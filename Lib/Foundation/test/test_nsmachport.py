import unittest
import objc

from Foundation import NSMachPort

class TestNSMachPort(unittest.TestCase):
    def testAlloc(self):
        obj = NSMachPort.alloc()
        self.assert_(obj is not None)

        obj = obj.init()
        self.assert_(obj is not None)

if __name__ == '__main__':
    unittest.main( )
