from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestContacts (TestCase):
        @min_os_level("10.11")
        def testClasses(self):
            self.assertIsInstance(Contacts.CNContact, objc.objc_class)

if __name__ == "__main__":
    main()
