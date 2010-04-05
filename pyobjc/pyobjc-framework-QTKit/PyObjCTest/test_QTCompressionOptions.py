
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCompressionOptions (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(QTCompressionOptions.isEqualToCompressionOptions_)


if __name__ == "__main__":
    main()
