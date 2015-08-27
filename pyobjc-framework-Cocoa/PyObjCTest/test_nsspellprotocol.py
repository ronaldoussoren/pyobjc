from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSSpellProtocol (TestCase):
    def testProtocols(self):
        objc.protocolNamed('NSChangeSpelling')
        objc.protocolNamed('NSIgnoreMisspelledWords')


if __name__ == "__main__":
    main()
