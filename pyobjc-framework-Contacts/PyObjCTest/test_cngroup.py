from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNGroup (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(Contacts.CNGroupIdentifierKey, unicode)
            self.assertIsInstance(Contacts.CNGroupNameKey, unicode)

if __name__ == "__main__":
    main()
