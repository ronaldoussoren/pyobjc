
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTTypesetter (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CTTypesetterRef)

    def testConstants(self):
        self.failUnlessIsInstance(kCTTypesetterOptionDisableBidiProcessing, unicode)

    def testFunctions(self):
        self.failUnlessIsInstance(CTTypesetterGetTypeID(), (int, long))

        astring = CFAttributedStringCreate(None, u"hello world", None)
        self.failUnlessIsInstance(astring, CFAttributedStringRef)

        self.failUnlessResultIsCFRetained(CTTypesetterCreateWithAttributedString)
        ref = CTTypesetterCreateWithAttributedString(astring)
        self.failUnlessIsInstance(ref, CTTypesetterRef)

        self.failUnlessResultIsCFRetained(CTTypesetterCreateWithAttributedStringAndOptions)
        options = { 'key': 'value' }
        ref = CTTypesetterCreateWithAttributedStringAndOptions(astring, options)
        self.failUnlessIsInstance(ref, CTTypesetterRef)

        line = CTTypesetterCreateLine(ref, CFRange(0, 5))
        self.failUnlessIsInstance(line, CTLineRef)

        v = CTTypesetterSuggestLineBreak(ref, 0, 100.0)
        self.failUnlessIsInstance(v, (int, long))

        v = CTTypesetterSuggestClusterBreak(ref, 0, 100.0)
        self.failUnlessIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
