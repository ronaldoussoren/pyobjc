from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNContactRelation (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(Contacts.CNLabelContactRelationFather, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationMother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationParent, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationBrother, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationSister, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationChild, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationFriend, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationSpouse, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationPartner, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationAssistant, unicode)
            self.assertIsInstance(Contacts.CNLabelContactRelationManager, unicode)

if __name__ == "__main__":
    main()
