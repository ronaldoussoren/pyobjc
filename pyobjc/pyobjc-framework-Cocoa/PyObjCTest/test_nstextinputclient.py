
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
    def drawsVerticallyForCharacterAtIndex_(self, i): return 1


class TestNSTextInputClient (TestCase):

    @min_os_level("10.5")
    def testMethods(self):
        self.assertArgHasType(TestNSTextInputClientHelper.insertText_replacementRange_, 1, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextInputClientHelper.doCommandBySelector_, 0,  objc._C_SEL)
        self.assertArgHasType(TestNSTextInputClientHelper.setMarkedText_selectedRange_replacementRange_, 1, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextInputClientHelper.setMarkedText_selectedRange_replacementRange_, 2, NSRange.__typestr__)
        self.assertResultHasType(TestNSTextInputClientHelper.selectedRange, NSRange.__typestr__)
        self.assertResultHasType(TestNSTextInputClientHelper.markedRange, NSRange.__typestr__)
        self.assertResultIsBOOL(TestNSTextInputClientHelper.hasMarkedText)
        self.assertArgHasType(TestNSTextInputClientHelper.attributedSubstringForProposedRange_actualRange_, 0, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextInputClientHelper.attributedSubstringForProposedRange_actualRange_, 1, b'o^' + NSRange.__typestr__)
        self.assertResultHasType(TestNSTextInputClientHelper.firstRectForCharacterRange_actualRange_, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextInputClientHelper.firstRectForCharacterRange_actualRange_, 0, NSRange.__typestr__)
        self.assertArgHasType(TestNSTextInputClientHelper.firstRectForCharacterRange_actualRange_, 1, b'o^' + NSRange.__typestr__)
        self.assertResultHasType(TestNSTextInputClientHelper.characterIndexForPoint_, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextInputClientHelper.characterIndexForPoint_, 0, NSPoint.__typestr__)
        self.assertResultHasType(TestNSTextInputClientHelper.fractionOfDistanceThroughGlyphForPoint_, objc._C_CGFloat)
        self.assertArgHasType(TestNSTextInputClientHelper.fractionOfDistanceThroughGlyphForPoint_, 0, NSPoint.__typestr__)
        self.assertResultHasType(TestNSTextInputClientHelper.baselineDeltaForCharacterAtIndex_, objc._C_CGFloat)
        self.assertArgHasType(TestNSTextInputClientHelper.baselineDeltaForCharacterAtIndex_, 0, objc._C_NSUInteger)
        self.assertResultHasType(TestNSTextInputClientHelper.windowLevel, objc._C_NSInteger)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(TestNSTextInputClientHelper.drawsVerticallyForCharacterAtIndex_)
        self.assertArgHasType(TestNSTextInputClientHelper.drawsVerticallyForCharacterAtIndex_, 0, objc._C_NSInteger)


if __name__ == "__main__":
    main()
