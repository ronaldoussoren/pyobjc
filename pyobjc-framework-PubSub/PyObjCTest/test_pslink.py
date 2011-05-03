
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSLink (TestCase):
    def testConstants(self):
        self.assertEqual(PSLinkToOther, 0)
        self.assertEqual(PSLinkToRSS, 1)
        self.assertEqual(PSLinkToAtom, 2)
        self.assertEqual(PSLinkToAtomService, 3)
        self.assertEqual(PSLinkToFOAF, 4)
        self.assertEqual(PSLinkToRSD, 5)
        self.assertEqual(PSLinkToSelf, 6)
        self.assertEqual(PSLinkToAlternate, 7)


if __name__ == "__main__":
    main()
