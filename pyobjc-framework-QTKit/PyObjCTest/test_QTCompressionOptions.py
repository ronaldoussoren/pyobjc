
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCompressionOptions (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(QTCompressionOptions.isEqualToCompressionOptions_)


if __name__ == "__main__":
    main()
