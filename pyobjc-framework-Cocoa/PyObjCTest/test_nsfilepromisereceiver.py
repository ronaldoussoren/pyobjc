from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSFilePromiseReceiver (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertArgIsBlock(NSFilePromiseReceiver.receivePromisedFilesAtDestination_options_operationQueue_reader_, 3, b'v@@')


if __name__ == "__main__":
    main()
