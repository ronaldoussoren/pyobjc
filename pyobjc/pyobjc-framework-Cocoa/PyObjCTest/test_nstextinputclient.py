
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextInputClientHelper (NSObject):
    def insertText_replacementRange_(self, txt, rng): pass
    def doCommandBySelector_(self, sel): pass
    def setMarkedText_selectedRange_replacementRange_(self, txt, rng1, rng2): pass
    def selectedRange(self): return 1
    def markedRange(self): return 1
    def hasMarkedText(self): return 1
    def attributedSubstringForProposedRange_actualRange_(self, rng1, rng2): return 1
    def firstRectForCharacterRange_actualRange_(self, rng1, rng2): return 1
    def characterIndexForPoint_(self, pt): return 1
    def fractionOfDistanceThroughGlyphForPoint_(self, pt): return 1
    def baselineDeltaForCharacterAtIndex_(self, idx): return 1
    def windowLevel(self): return 1


class TestNSTextInputClient (TestCase):

    @min_os_level("10.5")
    def testMethods(self):
        self.failUnlessArgHasType(TestNSTextInputClientHelper.insertText_replacementRange_, 1, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.doCommandBySelector_, 0,  objc._C_SEL)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.setMarkedText_selectedRange_replacementRange_, 1, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.setMarkedText_selectedRange_replacementRange_, 2, NSRange.__typestr__)
        self.failUnlessResultHasType(TestNSTextInputClientHelper.selectedRange, NSRange.__typestr__)
        self.failUnlessResultHasType(TestNSTextInputClientHelper.markedRange, NSRange.__typestr__)
        self.failUnlessResultIsBOOL(TestNSTextInputClientHelper.hasMarkedText)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.attributedSubstringForProposedRange_actualRange_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.attributedSubstringForProposedRange_actualRange_, 1, 'o^' + NSRange.__typestr__)
        self.failUnlessResultHasType(TestNSTextInputClientHelper.firstRectForCharacterRange_actualRange_, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.firstRectForCharacterRange_actualRange_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.firstRectForCharacterRange_actualRange_, 1, 'o^' + NSRange.__typestr__)
        self.failUnlessResultHasType(TestNSTextInputClientHelper.characterIndexForPoint_, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.characterIndexForPoint_, 0, NSPoint.__typestr__)
        self.failUnlessResultHasType(TestNSTextInputClientHelper.fractionOfDistanceThroughGlyphForPoint_, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.fractionOfDistanceThroughGlyphForPoint_, 0, NSPoint.__typestr__)
        self.failUnlessResultHasType(TestNSTextInputClientHelper.baselineDeltaForCharacterAtIndex_, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSTextInputClientHelper.baselineDeltaForCharacterAtIndex_, 0, objc._C_NSUInteger)
        self.failUnlessResultHasType(TestNSTextInputClientHelper.windowLevel, objc._C_NSInteger)


if __name__ == "__main__":
    main()
