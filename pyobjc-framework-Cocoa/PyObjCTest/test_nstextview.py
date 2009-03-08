
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSSelectByCharacter, 0)
        self.failUnlessEqual(NSSelectByWord, 1)
        self.failUnlessEqual(NSSelectByParagraph, 2)
        self.failUnlessEqual(NSSelectionAffinityUpstream, 0)
        self.failUnlessEqual(NSSelectionAffinityDownstream, 1)
        self.failUnlessEqual(NSFindPanelActionShowFindPanel, 1)
        self.failUnlessEqual(NSFindPanelActionNext, 2)
        self.failUnlessEqual(NSFindPanelActionPrevious, 3)
        self.failUnlessEqual(NSFindPanelActionReplaceAll, 4)
        self.failUnlessEqual(NSFindPanelActionReplace, 5)
        self.failUnlessEqual(NSFindPanelActionReplaceAndFind, 6)
        self.failUnlessEqual(NSFindPanelActionSetFindString, 7)
        self.failUnlessEqual(NSFindPanelActionReplaceAllInSelection, 8)
        self.failUnlessEqual(NSFindPanelActionSelectAll, 9)
        self.failUnlessEqual(NSFindPanelActionSelectAllInSelection, 10)

        self.failUnlessIsInstance(NSFindPanelSearchOptionsPboardType, unicode)

        self.failUnlessIsInstance(NSFindPanelCaseInsensitiveSearch, unicode)
        self.failUnlessIsInstance(NSFindPanelSubstringMatch, unicode)

        self.failUnlessEqual(NSFindPanelSubstringMatchTypeContains, 0)
        self.failUnlessEqual(NSFindPanelSubstringMatchTypeStartsWith, 1)
        self.failUnlessEqual(NSFindPanelSubstringMatchTypeFullWord, 2)
        self.failUnlessEqual(NSFindPanelSubstringMatchTypeEndsWith, 3)

        self.failUnlessIsInstance(NSAllRomanInputSourcesLocaleIdentifier, unicode)

        self.failUnlessIsInstance(NSTextViewWillChangeNotifyingTextViewNotification, unicode)
        self.failUnlessIsInstance(NSTextViewDidChangeSelectionNotification, unicode)
        self.failUnlessIsInstance(NSTextViewDidChangeTypingAttributesNotification, unicode)
        

    def testMethods(self):
        self.fail("- (NSArray *)completionsForPartialWordRange:(NSRange)charRange indexOfSelectedItem:(NSInteger *)index;")
        self.fail("- (NSImage *)dragImageForSelectionWithEvent:(NSEvent *)event origin:(NSPointPointer)origin;")
        self.fail("- (void)smartInsertForString:(NSString *)pasteString replacingRange:(NSRange)charRangeToReplace beforeString:(NSString **)beforeString afterString:(NSString **)afterString;")




if __name__ == "__main__":
    main()
