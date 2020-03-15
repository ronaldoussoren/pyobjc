import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFilePromiseReceiver(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            AppKit.NSFilePromiseReceiver.receivePromisedFilesAtDestination_options_operationQueue_reader_,  # noqa: B950
            3,
            b"v@@",
        )
