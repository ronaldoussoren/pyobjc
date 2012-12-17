from PyObjCTools.TestSupport import *

from objc import *
from Foundation import *

class TestTollFreeBridging( TestCase ):
    def testImplicitFromCF(self):

        c = CFArrayCreateMutable(None, 0, None)
        self.assert_(isinstance(c, CFMutableArrayRef))

        nsa = NSMutableArray.array()
        nsa.addObject_(c)

        o = nsa[0]
        self.assert_(isinstance(o, NSMutableArray))

if __name__ == '__main__':
    main( )
