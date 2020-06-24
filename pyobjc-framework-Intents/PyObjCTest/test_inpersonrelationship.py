from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINPersonRelationship(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertIsInstance(Intents.INPersonRelationshipFather, str)
        self.assertIsInstance(Intents.INPersonRelationshipMother, str)
        self.assertIsInstance(Intents.INPersonRelationshipParent, str)
        self.assertIsInstance(Intents.INPersonRelationshipBrother, str)
        self.assertIsInstance(Intents.INPersonRelationshipSister, str)
        self.assertIsInstance(Intents.INPersonRelationshipChild, str)
        self.assertIsInstance(Intents.INPersonRelationshipFriend, str)
        self.assertIsInstance(Intents.INPersonRelationshipSpouse, str)
        self.assertIsInstance(Intents.INPersonRelationshipPartner, str)
        self.assertIsInstance(Intents.INPersonRelationshipAssistant, str)
        self.assertIsInstance(Intents.INPersonRelationshipManager, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(Intents.INPersonRelationshipSon, str)
        self.assertIsInstance(Intents.INPersonRelationshipDaughter, str)
