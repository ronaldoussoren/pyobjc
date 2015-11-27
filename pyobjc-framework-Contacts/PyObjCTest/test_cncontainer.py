from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNContainer (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertEqual(Contacts.CNContainerTypeUnassigned, 0)
            self.assertEqual(Contacts.CNContainerTypeLocal, 1)
            self.assertEqual(Contacts.CNContainerTypeExchange, 2)
            self.assertEqual(Contacts.CNContainerTypeCardDAV, 3)

            self.assertIsInstance(Contacts.CNContainerIdentifierKey, unicode)
            self.assertIsInstance(Contacts.CNContainerNameKey, unicode)
            self.assertIsInstance(Contacts.CNContainerTypeKey, unicode)


if __name__ == "__main__":
    main()
