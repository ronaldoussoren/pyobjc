import objc
import PyObjCTest.fnd as Foundation
from PyObjCTools.TestSupport import *
import os

NSObject = objc.lookUpClass('NSObject')

def S(*args):
    return ''.join(args)

FUNCTIONS=[
    ( u'NSHomeDirectory', S(objc._C_ID)),
    ( u'NSIsFreedObject', S(objc._C_NSBOOL, objc._C_ID) ),
    ( u'NSCountFrames', S(objc._C_UINT) ),
    ( u'NSClassFromString', S(objc._C_CLASS, objc._C_ID) ),
]

class TestBundleFunctions (TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

    def testSimple(self):
        d = {}
        objc.loadBundleFunctions(self.bundle, d, FUNCTIONS)

        self.assert_('NSIsFreedObject' in d)
        self.assert_('NSCountFrames' in d)
        self.assert_('NSHomeDirectory' in d)

        # Don't use this API, it is unsupported and causes warnings.
        #fn = d[u'NSIsFreedObject']
        #obj = NSObject.alloc().init()
        #value = fn(obj)
        #self.assert_(not value)

        fn = d[u'NSHomeDirectory']
        value = fn()
        self.assertEquals(value, os.path.expanduser('~'))

        fn = d[u'NSClassFromString']
        value = fn(u'NSObject')
        self.assert_(value is NSObject)

        # Need to look for a different example, NSCountFrames crashes
        # (that is the actual function, not the dynamic wrapper)
        #fn = d[u'NSCountFrames']
        #import Foundation
        #fn = Foundation.NSCountFrames
        #value = fn()
        #self.assert_(isistance(value, int))


if __name__ == "__main__":
    main()


