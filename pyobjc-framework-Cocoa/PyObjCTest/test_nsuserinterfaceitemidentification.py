from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSUserInterfaceItemIdentification (TestCase):
    @min_os_level('10.7')
    def testProtocols(self):
        objc.protocolNamed('NSUserInterfaceItemIdentification')

if __name__ == "__main__":
    main()
