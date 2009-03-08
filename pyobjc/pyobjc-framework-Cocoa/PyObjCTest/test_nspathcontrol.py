
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPathControl (TestCase):

    @min_os_level("10.5")
    def testMethods(self):
        m = NSPathControl.setDoubleAction_.__metadata__()
        self.failUnlessEqual(m['arguments'][2]['sel_of_type'], 'v@:@')


if __name__ == "__main__":
    main()
