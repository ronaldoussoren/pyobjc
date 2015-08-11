from PyObjCTools.TestSupport import *
from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSExtensionRequestHandling (TestCase):
    @min_sdk_level('10.10')
    def testProtocols10_10(self):
        objc.protocolNamed('NSExtensionRequestHandling')

if __name__ == "__main__":
    main()
