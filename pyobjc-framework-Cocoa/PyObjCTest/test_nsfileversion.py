import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileVersion(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSFileVersionAddingOptions)
        self.assertIsEnumType(Foundation.NSFileVersionReplacingOptions)

    @min_os_level("10.7")
    def testContants10_7(self):
        self.assertEqual(Foundation.NSFileVersionAddingByMoving, 1 << 0)
        self.assertEqual(Foundation.NSFileVersionReplacingByMoving, 1 << 0)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsOut(
            Foundation.NSFileVersion.addVersionOfItemAtURL_withContentsOfURL_options_error_,
            3,
        )
        self.assertArgIsOut(Foundation.NSFileVersion.replaceItemAtURL_options_error_, 2)
        self.assertArgIsOut(Foundation.NSFileVersion.removeAndReturnError_, 0)
        self.assertResultIsBOOL(Foundation.NSFileVersion.removeAndReturnError_)

        self.assertArgIsOut(
            Foundation.NSFileVersion.removeOtherVersionsOfItemAtURL_error_, 1
        )
        self.assertResultIsBOOL(
            Foundation.NSFileVersion.removeOtherVersionsOfItemAtURL_error_
        )

        self.assertResultIsBOOL(Foundation.NSFileVersion.isConflict)

        self.assertArgIsBOOL(Foundation.NSFileVersion.setResolved_, 0)
        self.assertResultIsBOOL(Foundation.NSFileVersion.isResolved)
        self.assertArgIsBOOL(Foundation.NSFileVersion.setDiscardable_, 0)
        self.assertResultIsBOOL(Foundation.NSFileVersion.isDiscardable)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            Foundation.NSFileVersion.getNonlocalVersionsOfItemAtURL_completionHandler_,
            1,
            b"v@@",
        )
        self.assertResultIsBOOL(Foundation.NSFileVersion.hasLocalContents)
        self.assertResultIsBOOL(Foundation.NSFileVersion.hasThumbnail)
