from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSLayoutContraintManual (TestCase):
    def testNSDictionaryOfVariableBindings(self):
        var1 = 'foo'
        var2 = 'bar'

        self.assertEqual(NSDictionaryOfVariableBindings('var1', 'var2'),
                {'var1': 'foo', 'var2': 'bar'})

        self.assertRaises(KeyError, NSDictionaryOfVariableBindings, 'var1', 'var3')

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(NSViewNoInstrinsicMetric, float)
        self.assertEqual(NSLayoutRelationLessThanOrEqual, -1)
        self.assertEqual(NSLayoutRelationEqual, 0)
        self.assertEqual(NSLayoutRelationGreaterThanOrEqual, 1)
        self.assertEqual(NSLayoutAttributeLeft, 1)
        self.assertEqual(NSLayoutAttributeRight, 2)
        self.assertEqual(NSLayoutAttributeTop, 3)
        self.assertEqual(NSLayoutAttributeBottom, 4)
        self.assertEqual(NSLayoutAttributeLeading, 5)
        self.assertEqual(NSLayoutAttributeTrailing, 6)
        self.assertEqual(NSLayoutAttributeWidth, 7)
        self.assertEqual(NSLayoutAttributeHeight, 8)
        self.assertEqual(NSLayoutAttributeCenterX, 9)
        self.assertEqual(NSLayoutAttributeCenterY, 10)
        self.assertEqual(NSLayoutAttributeBaseline, 11)
        self.assertEqual(NSLayoutAttributeNotAnAttribute, 0)
        self.assertEqual(NSLayoutFormatAlignAllLeft, (1 << NSLayoutAttributeLeft))
        self.assertEqual(NSLayoutFormatAlignAllRight, (1 << NSLayoutAttributeRight))
        self.assertEqual(NSLayoutFormatAlignAllTop, (1 << NSLayoutAttributeTop))
        self.assertEqual(NSLayoutFormatAlignAllBottom, (1 << NSLayoutAttributeBottom))
        self.assertEqual(NSLayoutFormatAlignAllLeading, (1 << NSLayoutAttributeLeading))
        self.assertEqual(NSLayoutFormatAlignAllTrailing, (1 << NSLayoutAttributeTrailing))
        self.assertEqual(NSLayoutFormatAlignAllCenterX, (1 << NSLayoutAttributeCenterX))
        self.assertEqual(NSLayoutFormatAlignAllCenterY, (1 << NSLayoutAttributeCenterY))
        self.assertEqual(NSLayoutFormatAlignAllBaseline, (1 << NSLayoutAttributeBaseline))
        self.assertEqual(NSLayoutFormatAlignmentMask, 0xFFFF)

        self.assertEqual(NSLayoutFormatDirectionLeadingToTrailing, 0 << 16)
        self.assertEqual(NSLayoutFormatDirectionLeftToRight, 1 << 16)
        self.assertEqual(NSLayoutFormatDirectionRightToLeft, 2 << 16)

        self.assertEqual(NSLayoutFormatDirectionMask, 0x3 << 16)
        self.assertEqual(NSLayoutConstraintOrientationHorizontal, 0)
        self.assertEqual(NSLayoutConstraintOrientationVertical, 1)

        self.assertEqual(NSLayoutPriorityRequired, 1000)
        self.assertEqual(NSLayoutPriorityDefaultHigh, 750)
        self.assertEqual(NSLayoutPriorityDragThatCanResizeWindow, 510)
        self.assertEqual(NSLayoutPriorityWindowSizeStayPut, 500)
        self.assertEqual(NSLayoutPriorityDragThatCannotResizeWindow, 490)
        self.assertEqual(NSLayoutPriorityDefaultLow, 250)
        self.assertEqual(NSLayoutPriorityFittingSizeCompression, 50)

    @min_os_level('10.7')
    def testRecords10_7(self):
        v = NSEdgeInsets()
        self.assertEqual(v.top, 0.0)
        self.assertEqual(v.left, 0.0)
        self.assertEqual(v.bottom, 0.0)
        self.assertEqual(v.right, 0.0)

        self.assertEqual(NSEdgeInsets.__typestr__,
                b'{_NSEdgeInsets=' + objc._C_CGFloat + objc._C_CGFloat + objc._C_CGFloat + objc._C_CGFloat + b'}')

    @min_os_level('10.7')
    def testFunctions10_7(self):
        v = NSEdgeInsetsMake(1, 2, 3, 4)
        self.assertIsInstance(v, NSEdgeInsets)
        self.assertEqual(v.top, 1.0)
        self.assertEqual(v.left, 2.0)
        self.assertEqual(v.bottom, 3.0)
        self.assertEqual(v.right, 4.0)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSLayoutConstraint.shouldBeArchived)
        self.assertArgIsBOOL(NSLayoutConstraint.setShouldBeArchived_, 0)

        self.assertResultIsBOOL(NSView.needsUpdateConstraints)
        self.assertArgIsBOOL(NSView.setNeedsUpdateConstraints_, 0)

        self.assertResultIsBOOL(NSView.needsLayout)
        self.assertArgIsBOOL(NSView.setNeedsLayout_, 0)

        self.assertResultIsBOOL(NSView.translatesAutoresizingMaskIntoConstraints)
        self.assertArgIsBOOL(NSView.setTranslatesAutoresizingMaskIntoConstraints_, 0)
        self.assertResultIsBOOL(NSView.requiresConstraintBasedLayout)
        self.assertResultIsBOOL(NSView.hasAmbiguousLayout)

if __name__ == "__main__":
    main()
