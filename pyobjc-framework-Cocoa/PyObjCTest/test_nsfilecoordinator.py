from PyObjCTools.TestSupport import *
import Foundation

class TestSFileCoordinator (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertEqual(NSFileCoordinatorReadingWithoutChanges, 1<<0)
        self.assertEqual(NSFileCoordinatorReadingResolvesSymbolicLink, 1<<1)
        self.assertEqual(NSFileCoordinatorWritingForDeleting, 1<<0)
        self.assertEqual(NSFileCoordinatorWritingForMoving, 1<<1)
        self.assertEqual(NSFileCoordinatorWritingForMerging, 1<<2)
        self.assertEqual(NSFileCoordinatorWritingForReplacing, 1<<3)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertArgIsOut(NSFileCoordinator.coordinateReadingItemAtURL_options_error_byAccessor_, 2)
        self.assertArgIsBlock(NSFileCoordinator.coordinateReadingItemAtURL_options_error_byAccessor_,
                3, 'v@')

        self.assertArgIsOut(NSFileCoordinator.coordinateWritingItemAtURL_options_error_byAccessor_, 2)
        self.assertArgIsBlock(NSFileCoordinator.coordinateWritingItemAtURL_options_error_byAccessor_,
                3, 'v@')

        self.assertArgIsOut(NSFileCoordinator.coordinateReadingItemAtURL_options_writingItemAtURL_options_error_byAccessor_, 4)
        self.assertArgIsBlock(NSFileCoordinator.coordinateReadingItemAtURL_options_writingItemAtURL_options_error_byAccessor_,
                5, 'v@@')

        self.assertArgIsOut(NSFileCoordinator.coordinateWritingItemAtURL_options_writingItemAtURL_options_error_byAccessor_, 4)
        self.assertArgIsBlock(NSFileCoordinator.coordinateWritingItemAtURL_options_writingItemAtURL_options_error_byAccessor_,
                5, 'v@@')

        self.assertArgIsOut(NSFileCoordinator.prepareForReadingItemsAtURLs_options_writingItemAtURLs_options_error_byAccessor_, 4)
        self.assertArgIsBlock(NSFileCoordinator.prepareForReadingItemsAtURLs_options_writingItemAtURLs_options_error_byAccessor_,
                5, 'v@@?') # FIXME: Cannot represent this completion handler!




if __name__ == "__main__":
    main()
