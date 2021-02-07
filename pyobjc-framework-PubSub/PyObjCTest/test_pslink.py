import PubSub
from PyObjCTools.TestSupport import TestCase


class TestPSLink(TestCase):
    def testConstants(self):
        self.assertEqual(PubSub.PSLinkToOther, 0)
        self.assertEqual(PubSub.PSLinkToRSS, 1)
        self.assertEqual(PubSub.PSLinkToAtom, 2)
        self.assertEqual(PubSub.PSLinkToAtomService, 3)
        self.assertEqual(PubSub.PSLinkToFOAF, 4)
        self.assertEqual(PubSub.PSLinkToRSD, 5)
        self.assertEqual(PubSub.PSLinkToSelf, 6)
        self.assertEqual(PubSub.PSLinkToAlternate, 7)
