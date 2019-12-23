from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSFileHandle(TestCase):
    def testConstants(self):
        self.assertIsInstance(NSFileHandleOperationException, unicode)
        self.assertIsInstance(NSFileHandleReadCompletionNotification, unicode)
        self.assertIsInstance(
            NSFileHandleReadToEndOfFileCompletionNotification, unicode
        )
        self.assertIsInstance(NSFileHandleConnectionAcceptedNotification, unicode)
        self.assertIsInstance(NSFileHandleDataAvailableNotification, unicode)
        self.assertIsInstance(NSFileHandleNotificationDataItem, unicode)
        self.assertIsInstance(NSFileHandleNotificationFileHandleItem, unicode)
        self.assertIsInstance(NSFileHandleNotificationMonitorModes, unicode)

    def testMethods(self):
        f = NSFileHandle.alloc().initWithFileDescriptor_closeOnDealloc_(0, False)
        self.assertArgIsBOOL(f.initWithFileDescriptor_closeOnDealloc_, 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsOut(NSFileHandle.fileHandleForReadingFromURL_error_, 1)
        self.assertArgIsOut(NSFileHandle.fileHandleForWritingToURL_error_, 1)
        self.assertArgIsOut(NSFileHandle.fileHandleForUpdatingURL_error_, 1)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBlock(NSFileHandle.setReadabilityHandler_, 0, b"v@")
        self.assertArgIsBlock(NSFileHandle.setWriteabilityHandler_, 0, b"v@")
        self.assertResultIsBlock(NSFileHandle.readabilityHandler, b"v@")
        self.assertResultIsBlock(NSFileHandle.writeabilityHandler, b"v@")

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsOut(NSFileHandle.readDataToEndOfFileAndReturnError_, 0)
        self.assertArgIsOut(NSFileHandle.readDataUpToLength_error_, 1)

        self.assertResultIsBOOL(NSFileHandle.writeData_error_)
        self.assertArgIsOut(NSFileHandle.writeData_error_, 1)

        self.assertResultIsBOOL(NSFileHandle.getOffset_error_)
        self.assertArgIsOut(NSFileHandle.getOffset_error_, 0)
        self.assertArgIsOut(NSFileHandle.getOffset_error_, 1)

        self.assertResultIsBOOL(NSFileHandle.seekToEndReturningOffset_error_)
        self.assertArgIsOut(NSFileHandle.seekToEndReturningOffset_error_, 0)
        self.assertArgIsOut(NSFileHandle.seekToEndReturningOffset_error_, 1)

        self.assertResultIsBOOL(NSFileHandle.seekToOffset_error_)
        self.assertArgIsOut(NSFileHandle.seekToOffset_error_, 1)

        self.assertResultIsBOOL(NSFileHandle.truncateAtOffset_error_)
        self.assertArgIsOut(NSFileHandle.truncateAtOffset_error_, 1)

        self.assertResultIsBOOL(NSFileHandle.synchronizeAndReturnError_)
        self.assertArgIsOut(NSFileHandle.synchronizeAndReturnError_, 0)

        self.assertResultIsBOOL(NSFileHandle.closeAndReturnError_)
        self.assertArgIsOut(NSFileHandle.closeAndReturnError_, 0)


if __name__ == "__main__":
    main()
