"""
Tests for objc.synthesize
"""
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSObject
import objc

class TestSynthesizeCopier (NSObject):
    def copy(self):
        return 42

class TestSynthesizeHelper (NSObject):
    objc.synthesize('someTitle', copy=True)
    objc.synthesize('stringValue', copy=False)
    objc.synthesize('read', readwrite=False)


class TestSynthesize (TestCase):
    def testNames(self):
        self.failUnless(hasattr(TestSynthesizeHelper, 'someTitle'))
        self.failUnless(hasattr(TestSynthesizeHelper, 'setSomeTitle_'))

        self.failUnless(hasattr(TestSynthesizeHelper, 'stringValue'))
        self.failUnless(hasattr(TestSynthesizeHelper, 'setStringValue_'))

        self.failUnless(hasattr(TestSynthesizeHelper, 'read'))
        self.failIf(hasattr(TestSynthesizeHelper, 'setRead_'))

    def testCopying(self):
        obj = TestSynthesizeHelper.alloc().init()

        v = TestSynthesizeCopier.alloc().init()

        obj.setStringValue_(v)
        self.failUnless(obj.stringValue() is v)

        obj.setSomeTitle_(v)
        self.failUnlessEqual(obj.someTitle(), 42)

if __name__ == "__main__":
    main()
