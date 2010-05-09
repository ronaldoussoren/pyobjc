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
        self.assertHasAttr(TestSynthesizeHelper, 'someTitle')
        self.assertHasAttr(TestSynthesizeHelper, 'setSomeTitle_')

        self.assertHasAttr(TestSynthesizeHelper, 'stringValue')
        self.assertHasAttr(TestSynthesizeHelper, 'setStringValue_')

        self.assertHasAttr(TestSynthesizeHelper, 'read')
        self.assertNotHasAttr(TestSynthesizeHelper, 'setRead_')

    def testCopying(self):
        obj = TestSynthesizeHelper.alloc().init()

        v = TestSynthesizeCopier.alloc().init()

        obj.setStringValue_(v)
        self.assertIs(obj.stringValue(), v)

        obj.setSomeTitle_(v)
        self.assertEqual(obj.someTitle(), 42)

if __name__ == "__main__":
    main()
