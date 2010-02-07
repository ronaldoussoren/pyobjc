
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMatrix (TestCase):
    def testConstants(self):
        self.assertEqual(NSRadioModeMatrix, 0)
        self.assertEqual(NSHighlightModeMatrix, 1)
        self.assertEqual(NSListModeMatrix, 2)
        self.assertEqual(NSTrackModeMatrix, 3)

    def testMethods(self):
        self.assertResultIsBOOL(NSMatrix.allowsEmptySelection)
        self.assertArgIsBOOL(NSMatrix.setAllowsEmptySelection_, 0)
        self.assertArgIsBOOL(NSMatrix.sendAction_to_forAllCells_, 2)
        self.assertArgIsSEL(NSMatrix.sendAction_to_forAllCells_, 0, objc._C_NSBOOL + b'@:@')
        self.assertArgIsSEL(NSMatrix.sortUsingSelector_, 0, objc._C_NSInteger + b'@:@')
        self.assertArgIsOut(NSMatrix.getNumberOfRows_columns_, 0)
        self.assertArgIsOut(NSMatrix.getNumberOfRows_columns_, 1)
        self.assertArgIsOut(NSMatrix.getRow_column_ofCell_, 0)
        self.assertArgIsOut(NSMatrix.getRow_column_ofCell_, 1)
        self.assertArgIsOut(NSMatrix.getRow_column_forPoint_, 0)
        self.assertArgIsOut(NSMatrix.getRow_column_forPoint_, 1)

        self.assertArgIsFunction(NSMatrix.sortUsingFunction_context_, 0, objc._C_NSInteger + b'@@@', False)
        self.assertArgHasType(NSMatrix.sortUsingFunction_context_, 1, objc._C_ID)


        self.assertResultIsBOOL(NSMatrix.isSelectionByRect)
        self.assertArgIsBOOL(NSMatrix.setSelectionByRect_, 0)
        self.assertArgIsBOOL(NSMatrix.setSelectionFrom_to_anchor_highlight_, 3)
        self.assertResultIsBOOL(NSMatrix.selectCellWithTag_)
        self.assertArgIsBOOL(NSMatrix.setScrollable_, 0)
        self.assertArgIsBOOL(NSMatrix.setDrawsCellBackground_, 0)
        self.assertResultIsBOOL(NSMatrix.drawsCellBackground)
        self.assertArgIsBOOL(NSMatrix.setDrawsBackground_, 0)
        self.assertResultIsBOOL(NSMatrix.drawsBackground)
        self.assertArgIsOut(NSMatrix.getNumberOfRows_columns_, 0)
        self.assertArgIsOut(NSMatrix.getNumberOfRows_columns_, 1)
        self.assertResultIsBOOL(NSMatrix.getRow_column_ofCell_)
        self.assertArgIsOut(NSMatrix.getRow_column_ofCell_, 0)
        self.assertArgIsOut(NSMatrix.getRow_column_ofCell_, 1)
        self.assertResultIsBOOL(NSMatrix.getRow_column_forPoint_)
        self.assertArgIsOut(NSMatrix.getRow_column_forPoint_, 0)
        self.assertArgIsOut(NSMatrix.getRow_column_forPoint_, 1)
        self.assertArgIsBOOL(NSMatrix.setAutosizesCells_, 0)
        self.assertResultIsBOOL(NSMatrix.autosizesCells)
        self.assertArgIsBOOL(NSMatrix.setValidateSize_, 0)
        self.assertArgIsBOOL(NSMatrix.highlightCell_atRow_column_, 0)
        self.assertArgIsBOOL(NSMatrix.setAutoscroll_, 0)
        self.assertResultIsBOOL(NSMatrix.isAutoscroll)
        self.assertResultIsBOOL(NSMatrix.performKeyEquivalent_)
        self.assertResultIsBOOL(NSMatrix.sendAction)
        self.assertResultIsBOOL(NSMatrix.textShouldBeginEditing_)
        self.assertResultIsBOOL(NSMatrix.textShouldEndEditing_)
        self.assertResultIsBOOL(NSMatrix.acceptsFirstMouse_)
        self.assertArgIsBOOL(NSMatrix.setTabKeyTraversesCells_, 0)
        self.assertResultIsBOOL(NSMatrix.tabKeyTraversesCells)




if __name__ == "__main__":
    main()
