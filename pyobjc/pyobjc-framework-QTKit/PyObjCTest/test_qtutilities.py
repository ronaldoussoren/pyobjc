
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTUtilities (TestCase):
    def testFunctions(self):
        v = QTStringForOSType(15490)
        self.failUnlessIsInstance(v, unicode)

        w = QTOSTypeForString(v)
        self.failUnlessIsInstance(w, (int, long))
        self.failUnlessEqual(w, 15490)


if __name__ == "__main__":
    main()
