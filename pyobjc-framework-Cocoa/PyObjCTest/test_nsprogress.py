import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSProgress(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSProgressFileOperationKind, str)
        self.assertIsTypedEnum(AppKit.NSProgressKind, str)
        self.assertIsTypedEnum(AppKit.NSProgressUserInfoKey, str)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(AppKit.NSProgressEstimatedTimeRemainingKey, str)
        self.assertIsInstance(AppKit.NSProgressThroughputKey, str)
        self.assertIsInstance(AppKit.NSProgressKindFile, str)
        self.assertIsInstance(AppKit.NSProgressFileOperationKindKey, str)
        self.assertIsInstance(AppKit.NSProgressFileOperationKindDownloading, str)
        self.assertIsInstance(
            AppKit.NSProgressFileOperationKindDecompressingAfterDownloading, str
        )
        self.assertIsInstance(AppKit.NSProgressFileOperationKindReceiving, str)
        self.assertIsInstance(AppKit.NSProgressFileOperationKindCopying, str)
        self.assertIsInstance(AppKit.NSProgressFileURLKey, str)
        self.assertIsInstance(AppKit.NSProgressFileTotalCountKey, str)
        self.assertIsInstance(AppKit.NSProgressFileCompletedCountKey, str)
        self.assertIsInstance(AppKit.NSProgressFileAnimationImageKey, str)
        self.assertIsInstance(AppKit.NSProgressFileAnimationImageOriginalRectKey, str)
        self.assertIsInstance(AppKit.NSProgressFileIconKey, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AppKit.NSProgressFileOperationKindUploading, str)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(AppKit.NSProgressFileOperationKindDuplicating, str)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSProgress.isCancellable)
        self.assertArgIsBOOL(AppKit.NSProgress.setCancellable_, 0)

        self.assertResultIsBOOL(AppKit.NSProgress.isPausable)
        self.assertArgIsBOOL(AppKit.NSProgress.setPausable_, 0)

        self.assertResultIsBOOL(AppKit.NSProgress.isCancelled)
        self.assertResultIsBOOL(AppKit.NSProgress.isPaused)

        self.assertResultIsBlock(AppKit.NSProgress.cancellationHandler, b"v")
        self.assertArgIsBlock(AppKit.NSProgress.setCancellationHandler_, 0, b"v")

        self.assertResultIsBlock(AppKit.NSProgress.pausingHandler, b"v")
        self.assertArgIsBlock(AppKit.NSProgress.setPausingHandler_, 0, b"v")

        self.assertResultIsBOOL(AppKit.NSProgress.isIndeterminate)

        self.assertArgIsBlock(
            AppKit.NSProgress.addSubscriberForFileURL_withPublishingHandler_, 1, b"@?@"
        )

        self.assertResultIsBOOL(AppKit.NSProgress.isOld)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBlock(AppKit.NSProgress.resumingHandler, b"v")
        self.assertArgIsBlock(AppKit.NSProgress.setResumingHandler_, 0, b"v")

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            AppKit.NSProgress.performAsCurrentWithPendingUnitCount_usingBlock_, 1, b"v"
        )

    @min_sdk_level("10.11")
    def testProtocolObjects(self):
        objc.protocolNamed("NSProgressReporting")
