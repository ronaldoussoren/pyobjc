from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSSpellProtocol(TestCase):
    def testProtocols(self):
        objc.protocolNamed("NSChangeSpelling")
        objc.protocolNamed("NSIgnoreMisspelledWords")


if __name__ == "__main__":
    main()
