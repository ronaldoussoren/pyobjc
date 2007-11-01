import unittest, objc
from Foundation import *

class TestNSZone (unittest.TestCase):
    def testWithZones(self):
        obj = NSObject.allocWithZone_(None).init()
        zone = obj.zone()
        self.assert_(zone is not None)
        self.assert_(zone.__pointer__ != 0)
        
        obj2 = NSObject.allocWithZone_(zone).init()
        zone2 = obj2.zone()
        self.assertEquals(zone.__pointer__, zone2.__pointer__)

        self.assertRaises(TypeError, NSObject.allocWithZone_, 10)
        #self.assertRaises(TypeError, NSObject.allocWithZone_, objc.NULL)

if __name__ == "__main__":
    unittest.main()
