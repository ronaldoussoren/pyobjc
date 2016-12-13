import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINPersonRelationship (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertIsInstance(Intents.INPersonRelationshipFather, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipMother, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipParent, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipBrother, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipSister, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipChild, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipFriend, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipSpouse, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipPartner, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipAssistant, unicode)
            self.assertIsInstance(Intents.INPersonRelationshipManager, unicode)


if __name__ == "__main__":
    main()
