from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLDTD (TestCase):

    def testOutputArgs(self):
        self.failUnlessArgIsOut(NSXMLDTD.initWithContentsOfURL_options_error_, 2)
        self.failUnlessArgIsOut(NSXMLDTD.initWithData_options_error_, 2)



if __name__ == "__main__":
    main()
