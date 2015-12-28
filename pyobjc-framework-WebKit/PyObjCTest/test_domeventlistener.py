from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMEventListener (TestCase):

    @min_os_level('10.10')
    def testProtocols(self):
        objc.protocolNamed('DOMEventListener')

if __name__ == "__main__":
    main()
