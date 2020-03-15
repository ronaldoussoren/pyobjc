import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileCoordinator(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(
            Foundation.NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly, 1 << 2
        )
        self.assertEqual(Foundation.NSFileCoordinatorReadingForUploading, 1 << 3)
        self.assertEqual(
            Foundation.NSFileCoordinatorWritingContentIndependentMetadataOnly, 1 << 4
        )

    @min_os_level("10.7")
    def testConstants(self):
        self.assertEqual(Foundation.NSFileCoordinatorReadingWithoutChanges, 1 << 0)
        self.assertEqual(
            Foundation.NSFileCoordinatorReadingResolvesSymbolicLink, 1 << 1
        )
        self.assertEqual(Foundation.NSFileCoordinatorWritingForDeleting, 1 << 0)
        self.assertEqual(Foundation.NSFileCoordinatorWritingForMoving, 1 << 1)
        self.assertEqual(Foundation.NSFileCoordinatorWritingForMerging, 1 << 2)
        self.assertEqual(Foundation.NSFileCoordinatorWritingForReplacing, 1 << 3)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            Foundation.NSFileCoordinator.coordinateAccessWithIntents_queue_byAccessor_,
            2,
            b"v@",
        )

    @min_os_level("10.7")
    def testMethods(self):
        self.assertArgIsOut(
            Foundation.NSFileCoordinator.coordinateReadingItemAtURL_options_error_byAccessor_,
            2,
        )
        self.assertArgIsBlock(
            Foundation.NSFileCoordinator.coordinateReadingItemAtURL_options_error_byAccessor_,
            3,
            b"v@",
        )

        self.assertArgIsOut(
            Foundation.NSFileCoordinator.coordinateWritingItemAtURL_options_error_byAccessor_,
            2,
        )
        self.assertArgIsBlock(
            Foundation.NSFileCoordinator.coordinateWritingItemAtURL_options_error_byAccessor_,
            3,
            b"v@",
        )

        self.assertArgIsOut(
            Foundation.NSFileCoordinator.coordinateReadingItemAtURL_options_writingItemAtURL_options_error_byAccessor_,  # noqa: B950
            4,
        )
        self.assertArgIsBlock(
            Foundation.NSFileCoordinator.coordinateReadingItemAtURL_options_writingItemAtURL_options_error_byAccessor_,  # noqa: B950
            5,
            b"v@@",
        )

        self.assertArgIsOut(
            Foundation.NSFileCoordinator.coordinateWritingItemAtURL_options_writingItemAtURL_options_error_byAccessor_,  # noqa: B950
            4,
        )
        self.assertArgIsBlock(
            Foundation.NSFileCoordinator.coordinateWritingItemAtURL_options_writingItemAtURL_options_error_byAccessor_,  # noqa: B950
            5,
            b"v@@",
        )

        self.assertArgIsOut(
            Foundation.NSFileCoordinator.prepareForReadingItemsAtURLs_options_writingItemsAtURLs_options_error_byAccessor_,  # noqa: B950
            4,
        )
        self.assertArgIsBlock(
            Foundation.NSFileCoordinator.prepareForReadingItemsAtURLs_options_writingItemsAtURLs_options_error_byAccessor_,  # noqa: B950
            5,
            b"v@?",
        )  # FIXME: Need test for the "nested" block
