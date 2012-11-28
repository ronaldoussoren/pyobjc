from __future__ import absolute_import, unicode_literals
import objc
from . import fnd as Foundation
from PyObjCTools.TestSupport import *
import os

NSObject = objc.lookUpClass('NSObject')

def S(*args):
    return b''.join(args)

FUNCTIONS=[
    ( 'NSHomeDirectory', S(objc._C_ID)),
    ( 'NSIsFreedObject', S(objc._C_NSBOOL, objc._C_ID) ),
    ( 'NSCountFrames', S(objc._C_UINT) ),
    ( 'NSClassFromString', S(objc._C_CLASS, objc._C_ID) ),
]

class TestBundleFunctions (TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

    def testSimple(self):
        for bundle in (None, self.bundle):
            d = {}
            objc.loadBundleFunctions(self.bundle, d, FUNCTIONS)

            self.assertIn('NSIsFreedObject', d)
            self.assertIn('NSCountFrames', d)
            self.assertIn('NSHomeDirectory', d)

            # Don't use this API, it is unsupported and causes warnings.
            #fn = d[u'NSIsFreedObject']
            #obj = NSObject.alloc().init()
            #value = fn(obj)
            #self.assertTrue(not value)

            fn = d['NSHomeDirectory']
            value = fn()
            self.assertEqual(value, os.path.expanduser('~'))

            fn = d['NSClassFromString']
            value = fn('NSObject')
            self.assertIs(value, NSObject)

            # Need to look for a different example, NSCountFrames crashes
            # (that is the actual function, not the dynamic wrapper)
            #fn = d[u'NSCountFrames']
            #import Foundation
            #fn = Foundation.NSCountFrames
            #value = fn()
            #self.assertIsInstance(value, int)


if __name__ == "__main__":
    main()
