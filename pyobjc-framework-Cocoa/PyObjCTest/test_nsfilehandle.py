from PyObjCTools.TestSupport import *

from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSFileHandle (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSFileHandleOperationException, unicode)
        self.assertIsInstance(NSFileHandleReadCompletionNotification, unicode)
        self.assertIsInstance(NSFileHandleReadToEndOfFileCompletionNotification, unicode)
        self.assertIsInstance(NSFileHandleConnectionAcceptedNotification, unicode)
        self.assertIsInstance(NSFileHandleDataAvailableNotification, unicode)
        self.assertIsInstance(NSFileHandleNotificationDataItem, unicode)
        self.assertIsInstance(NSFileHandleNotificationFileHandleItem, unicode)
        self.assertIsInstance(NSFileHandleNotificationMonitorModes, unicode)

    def testMethods(self):
        f = NSFileHandle.alloc().initWithFileDescriptor_closeOnDealloc_(0, False)
        self.assertArgIsBOOL(f.initWithFileDescriptor_closeOnDealloc_, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsOut(NSFileHandle.fileHandleForReadingFromURL_error_, 1)
        self.assertArgIsOut(NSFileHandle.fileHandleForWritingToURL_error_, 1)
        self.assertArgIsOut(NSFileHandle.fileHandleForUpdatingURL_error_, 1)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBlock(NSFileHandle.setReadabilityHandler_, 0, b'v@')
        self.assertArgIsBlock(NSFileHandle.setWriteabilityHandler_, 0, b'v@')
        self.assertResultIsBlock(NSFileHandle.readabilityHandler, b'v@')
        self.assertResultIsBlock(NSFileHandle.writeabilityHandler, b'v@')


if __name__ == "__main__":
    main()
