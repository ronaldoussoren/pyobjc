from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSExtensionRequestHandling (TestCase):
    @min_sdk_level('10.10')
    @onlyOn64Bit
    def testProtocols10_10(self):
        objc.protocolNamed('NSExtensionRequestHandling')

if __name__ == "__main__":
    main()
