from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSProgress(TestCase):
    @min_os_level('10.9')
    def testMethods(self):
        self.assertResultIsBOOL(NSProgress.isCancellable)
        self.assertArgIsBOOL(NSProgress.setCancellable_, 0)

        self.assertResultIsBOOL(NSProgress.isPausable)
        self.assertArgIsBOOL(NSProgress.setPausable_, 0)

        self.assertResultIsBOOL(NSProgress.isCancelled)
        self.assertResultIsBOOL(NSProgress.isPaused)

        self.assertResultIsBlock(NSProgress.cancellationHandler, b'v')
        self.assertArgIsBlock(NSProgress.setCancellationHandler_, 0, b'v')

        self.assertResultIsBlock(NSProgress.pausingHandler, b'v')
        self.assertArgIsBlock(NSProgress.setPausingHandler_, 0, b'v')

        self.assertResultIsBOOL(NSProgress.isIndeterminate)

        self.assertArgIsBlock(NSProgress.addSubscriberForFileURL_withPublishingHandler_, 1, b'@?@')

        self.assertResultIsBOOL(NSProgress.isOld)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBlock(NSProgress.resumingHandler, b'v')
        self.assertArgIsBlock(NSProgress.setResumingHandler_, 0, b'v')

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertArgIsBlock(NSProgress.performAsCurrentWithPendingUnitCount_usingBlock_, 1, b'v')

    @min_sdk_level('10.11')
    def testProtocolObjects(self):
        objc.protocolNamed('NSProgressReporting')

    @min_os_level('10.9')
    def testConstants(self):
        self.assertIsInstance(NSProgressEstimatedTimeRemainingKey, unicode)
        self.assertIsInstance(NSProgressThroughputKey, unicode)
        self.assertIsInstance(NSProgressKindFile, unicode)
        self.assertIsInstance(NSProgressFileOperationKindKey, unicode)
        self.assertIsInstance(NSProgressFileOperationKindDownloading, unicode)
        self.assertIsInstance(NSProgressFileOperationKindDecompressingAfterDownloading, unicode)
        self.assertIsInstance(NSProgressFileOperationKindReceiving, unicode)
        self.assertIsInstance(NSProgressFileOperationKindCopying, unicode)
        self.assertIsInstance(NSProgressFileURLKey, unicode)
        self.assertIsInstance(NSProgressFileTotalCountKey, unicode)
        self.assertIsInstance(NSProgressFileCompletedCountKey, unicode)
        self.assertIsInstance(NSProgressFileAnimationImageKey, unicode)
        self.assertIsInstance(NSProgressFileAnimationImageOriginalRectKey, unicode)
        self.assertIsInstance(NSProgressFileIconKey, unicode)

if __name__ == "__main__":
    main()
