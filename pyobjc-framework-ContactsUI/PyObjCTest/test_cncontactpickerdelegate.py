from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import ContactsUI

    class TestCNContactPickerDelegate (TestCase):
        @min_os_level("10.11")
        def testProtocols(self):
            objc.protocolNamed('CNContactPickerDelegate')

if __name__ == "__main__":
    main()
