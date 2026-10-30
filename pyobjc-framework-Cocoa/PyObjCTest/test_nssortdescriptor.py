import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSSortDescriptor(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(Foundation.NSSortDescriptor.initWithKey_ascending_, 1)
        self.assertArgIsBOOL(
            Foundation.NSSortDescriptor.initWithKey_ascending_selector_, 1
        )
        self.assertArgIsSEL(
            Foundation.NSSortDescriptor.initWithKey_ascending_selector_, 2, b"i@:@"
        )

        self.assertResultIsBOOL(Foundation.NSSortDescriptor.ascending)

        self.assertArgIsBOOL(
            Foundation.NSSortDescriptor.sortDescriptorWithKey_ascending_, 1
        )
        self.assertArgIsBOOL(
            Foundation.NSSortDescriptor.sortDescriptorWithKey_ascending_selector_, 1
        )

        self.assertArgIsBOOL(
            Foundation.NSSortDescriptor.sortDescriptorWithKey_ascending_comparator_, 1
        )
        self.assertArgIsBlock(
            Foundation.NSSortDescriptor.sortDescriptorWithKey_ascending_comparator_,
            2,
            b"i@@",
        )
        self.assertArgIsBOOL(
            Foundation.NSSortDescriptor.initWithKey_ascending_comparator_, 1
        )
        self.assertArgIsBlock(
            Foundation.NSSortDescriptor.initWithKey_ascending_comparator_, 2, b"i@@"
        )
        self.assertResultIsBlock(Foundation.NSSortDescriptor.comparator, b"i@@")
