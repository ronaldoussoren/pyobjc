from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMXPathNSResolver (TestCase):
    @min_sdk_level('10.10')
    def testProtocols(self):
        objc.protocolNamed('DOMXPathNSResolver')

if __name__ == "__main__":
    main()
