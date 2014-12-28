from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMProgressEvent (TestCase):
    @min_os_level('10.6')
    def testMethod10_6(self):
        self.assertResultIsBOOL(DOMProgressEvent.lengthComputable)

if __name__ == "__main__":
    main()
