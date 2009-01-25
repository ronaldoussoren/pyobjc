
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSLink (TestCase):
    def testConstants(self):
        self.failUnlessEqual(PSLinkToOther, 0)
        self.failUnlessEqual(PSLinkToRSS, 1)
        self.failUnlessEqual(PSLinkToAtom, 2)
        self.failUnlessEqual(PSLinkToAtomService, 3)
        self.failUnlessEqual(PSLinkToFOAF, 4)
        self.failUnlessEqual(PSLinkToRSD, 5)
        self.failUnlessEqual(PSLinkToSelf, 6)
        self.failUnlessEqual(PSLinkToAlternate, 7)


if __name__ == "__main__":
    main()
