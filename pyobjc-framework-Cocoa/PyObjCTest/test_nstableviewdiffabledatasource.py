import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSTableViewDiffableDataSource(TestCase):
    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertArgIsBlock(
            AppKit.NSTableViewDiffableDataSource.initWithTableView_cellProvider_,
            1,
            b"@@@" + objc._C_NSInteger + b"@",
        )

        self.assertArgIsBOOL(
            AppKit.NSTableViewDiffableDataSource.applySnapshot_animatingDifferences_, 1
        )

        self.assertArgIsBOOL(
            AppKit.NSTableViewDiffableDataSource.applySnapshot_animatingDifferences_completion_,
            1,
        )
        self.assertArgIsBlock(
            AppKit.NSTableViewDiffableDataSource.applySnapshot_animatingDifferences_completion_,
            2,
            b"v",
        )

        self.assertResultIsBlock(
            AppKit.NSTableViewDiffableDataSource.rowViewProvider,
            b"@@" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(
            AppKit.NSTableViewDiffableDataSource.setRowViewProvider_,
            0,
            b"@@" + objc._C_NSInteger + b"@",
        )
