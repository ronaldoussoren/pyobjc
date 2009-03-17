
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMatrix (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSRadioModeMatrix, 0)
        self.failUnlessEqual(NSHighlightModeMatrix, 1)
        self.failUnlessEqual(NSListModeMatrix, 2)
        self.failUnlessEqual(NSTrackModeMatrix, 3)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSMatrix.allowsEmptySelection)
        self.failUnlessArgIsBOOL(NSMatrix.setAllowsEmptySelection_, 0)
        self.failUnlessArgIsBOOL(NSMatrix.sendAction_to_forAllCells_, 2)
        self.failUnlessArgIsSEL(NSMatrix.sendAction_to_forAllCells_, 0, objc._C_NSBOOL + '@:@')
        self.failUnlessArgIsSEL(NSMatrix.sortUsingSelector_, 0, 'i@:@')
        self.failUnlessArgIsOut(NSMatrix.getNumberOfRows_columns_, 0)
        self.failUnlessArgIsOut(NSMatrix.getNumberOfRows_columns_, 1)
        self.failUnlessArgIsOut(NSMatrix.getRow_column_ofCell_, 0)
        self.failUnlessArgIsOut(NSMatrix.getRow_column_ofCell_, 1)
        self.failUnlessArgIsOut(NSMatrix.getRow_column_forPoint_, 0)
        self.failUnlessArgIsOut(NSMatrix.getRow_column_forPoint_, 1)

        self.failUnlessArgIsFunction(NSMatrix.sortUsingFunction_context_, 0, 'i@@@', False)
        self.failUnlessArgHasType(NSMatrix.sortUsingFunction_context_, 1, objc._C_ID)


        self.failUnlessResultIsBOOL(NSMatrix.isSelectionByRect)
        self.failUnlessArgIsBOOL(NSMatrix.setSelectionByRect_, 0)
        self.failUnlessArgIsBOOL(NSMatrix.setSelectionFrom_to_anchor_highlight_, 3)
        self.failUnlessResultIsBOOL(NSMatrix.selectCellWithTag_)
        self.failUnlessArgIsBOOL(NSMatrix.setScrollable_, 0)
        self.failUnlessArgIsBOOL(NSMatrix.setDrawsCellBackground_, 0)
        self.failUnlessResultIsBOOL(NSMatrix.drawsCellBackground)
        self.failUnlessArgIsBOOL(NSMatrix.setDrawsBackground_, 0)
        self.failUnlessResultIsBOOL(NSMatrix.drawsBackground)
        self.failUnlessArgIsOut(NSMatrix.getNumberOfRows_columns_, 0)
        self.failUnlessArgIsOut(NSMatrix.getNumberOfRows_columns_, 1)
        self.failUnlessResultIsBOOL(NSMatrix.getRow_column_ofCell_)
        self.failUnlessArgIsOut(NSMatrix.getRow_column_ofCell_, 0)
        self.failUnlessArgIsOut(NSMatrix.getRow_column_ofCell_, 1)
        self.failUnlessResultIsBOOL(NSMatrix.getRow_column_forPoint_)
        self.failUnlessArgIsOut(NSMatrix.getRow_column_forPoint_, 0)
        self.failUnlessArgIsOut(NSMatrix.getRow_column_forPoint_, 1)
        self.failUnlessArgIsBOOL(NSMatrix.setAutosizesCells_, 0)
        self.failUnlessResultIsBOOL(NSMatrix.autosizesCells)
        self.failUnlessArgIsBOOL(NSMatrix.setValidateSize_, 0)
        self.failUnlessArgIsBOOL(NSMatrix.highlightCell_atRow_column_, 0)
        self.failUnlessArgIsBOOL(NSMatrix.setAutoscroll_, 0)
        self.failUnlessResultIsBOOL(NSMatrix.isAutoscroll)
        self.failUnlessResultIsBOOL(NSMatrix.performKeyEquivalent_)
        self.failUnlessResultIsBOOL(NSMatrix.sendAction)
        self.failUnlessResultIsBOOL(NSMatrix.textShouldBeginEditing_)
        self.failUnlessResultIsBOOL(NSMatrix.textShouldEndEditing_)
        self.failUnlessResultIsBOOL(NSMatrix.acceptsFirstMouse_)
        self.failUnlessArgIsBOOL(NSMatrix.setTabKeyTraversesCells_, 0)
        self.failUnlessResultIsBOOL(NSMatrix.tabKeyTraversesCells)




if __name__ == "__main__":
    main()
