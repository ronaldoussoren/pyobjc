import unittest

import objc

class TestRegressions(unittest.TestCase):
    def testNSObjectRespondsToCommonMethods(self):
        NSObject=objc.runtime.NSObject
        self.assert_(NSObject.pyobjc_classMethods.respondsToSelector_('alloc'))
        self.assert_(NSObject.instancesRespondToSelector_('init'))
        self.assert_(not NSObject.instancesRespondToSelector_('frodel'))


    def testFSRepr(self):
        import Foundation
        fm = Foundation.NSFileManager.defaultManager()
        self.assertRaises(TypeError, fm.stringWithFileSystemRepresentation_length_, "/var")
        self.assertEquals(u"/var", fm.stringWithFileSystemRepresentation_length_("/var/boo", 4))

    def testUninitWarning(self):
        """
        Check that calling methods on unitialized objects raises an error
        """
        import warnings
        import Foundation

        o = Foundation.NSObject.alloc() # Not yet initialized
        warnings.filterwarnings('error', category=RuntimeWarning)
        try:
            self.assertRaises(RuntimeWarning, o.description)
        finally:
            del warnings.filters[0]

    def testMemoryInit(self):
        """
        Regression test for bug #814683, that didn't initialize the memory
        space for output parameters correctly.
        """
        import Foundation
        if not hasattr(Foundation, 'NSPropertyListSerialization'): return

        plist = 0

        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0)
        self.assertEquals(r[1], None)
        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0)
        self.assertEquals(r[1], None)


    def testDeallocUninit(self):
        import objc

        for clsName in [ 'NSURL', 'NSObject', 'NSArray' ]:
            d = getattr(objc.runtime, clsName).alloc()
            del d

if __name__ == '__main__':
    unittest.main()
