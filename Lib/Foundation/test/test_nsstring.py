import unittest
import objc

from Foundation import NSString

class TestNSString(unittest.TestCase):
    def testCompare(self):
        self.assert_( 
            NSString.localizedCaseInsensitiveCompare_('foo','bar') == 1,
            "NSString doesn't compare correctly")
        self.assert_( 
            NSString.localizedCaseInsensitiveCompare_('foo','Foo') == 0,
            "NSString doesn't compare correctly")
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNSString))
    return suite

if __name__ == '__main__':
    unittest.main( )

