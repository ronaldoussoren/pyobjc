import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileHandle(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSFileHandleOperationException, str)
        self.assertIsInstance(Foundation.NSFileHandleReadCompletionNotification, str)
        self.assertIsInstance(
            Foundation.NSFileHandleReadToEndOfFileCompletionNotification, str
        )
        self.assertIsInstance(
            Foundation.NSFileHandleConnectionAcceptedNotification, str
        )
        self.assertIsInstance(Foundation.NSFileHandleDataAvailableNotification, str)
        self.assertIsInstance(Foundation.NSFileHandleNotificationDataItem, str)
        self.assertIsInstance(Foundation.NSFileHandleNotificationFileHandleItem, str)
        self.assertIsInstance(Foundation.NSFileHandleNotificationMonitorModes, str)

    def testMethods(self):
        f = Foundation.NSFileHandle.alloc().initWithFileDescriptor_closeOnDealloc_(
            0, False
        )
        self.assertArgIsBOOL(f.initWithFileDescriptor_closeOnDealloc_, 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsOut(
            Foundation.NSFileHandle.fileHandleForReadingFromURL_error_, 1
        )
        self.assertArgIsOut(Foundation.NSFileHandle.fileHandleForWritingToURL_error_, 1)
        self.assertArgIsOut(Foundation.NSFileHandle.fileHandleForUpdatingURL_error_, 1)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBlock(Foundation.NSFileHandle.setReadabilityHandler_, 0, b"v@")
        self.assertArgIsBlock(Foundation.NSFileHandle.setWriteabilityHandler_, 0, b"v@")
        self.assertResultIsBlock(Foundation.NSFileHandle.readabilityHandler, b"v@")
        self.assertResultIsBlock(Foundation.NSFileHandle.writeabilityHandler, b"v@")

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsOut(
            Foundation.NSFileHandle.readDataToEndOfFileAndReturnError_, 0
        )
        self.assertArgIsOut(Foundation.NSFileHandle.readDataUpToLength_error_, 1)

        self.assertResultIsBOOL(Foundation.NSFileHandle.writeData_error_)
        self.assertArgIsOut(Foundation.NSFileHandle.writeData_error_, 1)

        self.assertResultIsBOOL(Foundation.NSFileHandle.getOffset_error_)
        self.assertArgIsOut(Foundation.NSFileHandle.getOffset_error_, 0)
        self.assertArgIsOut(Foundation.NSFileHandle.getOffset_error_, 1)

        self.assertResultIsBOOL(Foundation.NSFileHandle.seekToEndReturningOffset_error_)
        self.assertArgIsOut(Foundation.NSFileHandle.seekToEndReturningOffset_error_, 0)
        self.assertArgIsOut(Foundation.NSFileHandle.seekToEndReturningOffset_error_, 1)

        self.assertResultIsBOOL(Foundation.NSFileHandle.seekToOffset_error_)
        self.assertArgIsOut(Foundation.NSFileHandle.seekToOffset_error_, 1)

        self.assertResultIsBOOL(Foundation.NSFileHandle.truncateAtOffset_error_)
        self.assertArgIsOut(Foundation.NSFileHandle.truncateAtOffset_error_, 1)

        self.assertResultIsBOOL(Foundation.NSFileHandle.synchronizeAndReturnError_)
        self.assertArgIsOut(Foundation.NSFileHandle.synchronizeAndReturnError_, 0)

        self.assertResultIsBOOL(Foundation.NSFileHandle.closeAndReturnError_)
        self.assertArgIsOut(Foundation.NSFileHandle.closeAndReturnError_, 0)
