import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSMatrix(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSRadioModeMatrix, 0)
        self.assertEqual(AppKit.NSHighlightModeMatrix, 1)
        self.assertEqual(AppKit.NSListModeMatrix, 2)
        self.assertEqual(AppKit.NSTrackModeMatrix, 3)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSMatrix.allowsEmptySelection)
        self.assertArgIsBOOL(AppKit.NSMatrix.setAllowsEmptySelection_, 0)
        self.assertArgIsBOOL(AppKit.NSMatrix.sendAction_to_forAllCells_, 2)
        self.assertArgIsSEL(
            AppKit.NSMatrix.sendAction_to_forAllCells_, 0, objc._C_NSBOOL + b"@:@"
        )
        self.assertArgIsSEL(
            AppKit.NSMatrix.sortUsingSelector_, 0, objc._C_NSInteger + b"@:@"
        )
        self.assertArgIsOut(AppKit.NSMatrix.getNumberOfRows_columns_, 0)
        self.assertArgIsOut(AppKit.NSMatrix.getNumberOfRows_columns_, 1)
        self.assertArgIsOut(AppKit.NSMatrix.getRow_column_ofCell_, 0)
        self.assertArgIsOut(AppKit.NSMatrix.getRow_column_ofCell_, 1)
        self.assertArgIsOut(AppKit.NSMatrix.getRow_column_forPoint_, 0)
        self.assertArgIsOut(AppKit.NSMatrix.getRow_column_forPoint_, 1)

        self.assertArgIsFunction(
            AppKit.NSMatrix.sortUsingFunction_context_,
            0,
            objc._C_NSInteger + b"@@@",
            False,
        )
        self.assertArgHasType(AppKit.NSMatrix.sortUsingFunction_context_, 1, objc._C_ID)

        self.assertResultIsBOOL(AppKit.NSMatrix.isSelectionByRect)
        self.assertArgIsBOOL(AppKit.NSMatrix.setSelectionByRect_, 0)
        self.assertArgIsBOOL(AppKit.NSMatrix.setSelectionFrom_to_anchor_highlight_, 3)
        self.assertResultIsBOOL(AppKit.NSMatrix.selectCellWithTag_)
        self.assertArgIsBOOL(AppKit.NSMatrix.setScrollable_, 0)
        self.assertArgIsBOOL(AppKit.NSMatrix.setDrawsCellBackground_, 0)
        self.assertResultIsBOOL(AppKit.NSMatrix.drawsCellBackground)
        self.assertArgIsBOOL(AppKit.NSMatrix.setDrawsBackground_, 0)
        self.assertResultIsBOOL(AppKit.NSMatrix.drawsBackground)
        self.assertArgIsOut(AppKit.NSMatrix.getNumberOfRows_columns_, 0)
        self.assertArgIsOut(AppKit.NSMatrix.getNumberOfRows_columns_, 1)
        self.assertResultIsBOOL(AppKit.NSMatrix.getRow_column_ofCell_)
        self.assertArgIsOut(AppKit.NSMatrix.getRow_column_ofCell_, 0)
        self.assertArgIsOut(AppKit.NSMatrix.getRow_column_ofCell_, 1)
        self.assertResultIsBOOL(AppKit.NSMatrix.getRow_column_forPoint_)
        self.assertArgIsOut(AppKit.NSMatrix.getRow_column_forPoint_, 0)
        self.assertArgIsOut(AppKit.NSMatrix.getRow_column_forPoint_, 1)
        self.assertArgIsBOOL(AppKit.NSMatrix.setAutosizesCells_, 0)
        self.assertResultIsBOOL(AppKit.NSMatrix.autosizesCells)
        self.assertArgIsBOOL(AppKit.NSMatrix.setValidateSize_, 0)
        self.assertArgIsBOOL(AppKit.NSMatrix.highlightCell_atRow_column_, 0)
        self.assertArgIsBOOL(AppKit.NSMatrix.setAutoscroll_, 0)
        self.assertResultIsBOOL(AppKit.NSMatrix.isAutoscroll)
        self.assertResultIsBOOL(AppKit.NSMatrix.performKeyEquivalent_)
        self.assertResultIsBOOL(AppKit.NSMatrix.sendAction)
        self.assertResultIsBOOL(AppKit.NSMatrix.textShouldBeginEditing_)
        self.assertResultIsBOOL(AppKit.NSMatrix.textShouldEndEditing_)
        self.assertResultIsBOOL(AppKit.NSMatrix.acceptsFirstMouse_)
        self.assertArgIsBOOL(AppKit.NSMatrix.setTabKeyTraversesCells_, 0)
        self.assertResultIsBOOL(AppKit.NSMatrix.tabKeyTraversesCells)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBOOL(AppKit.NSMatrix.setAutorecalculatesCellSize_, 0)
        self.assertResultIsBOOL(AppKit.NSMatrix.autorecalculatesCellSize)

    @min_sdk_level("10.6")
    def testProtocols(self):
        objc.protocolNamed("NSMatrixDelegate")
