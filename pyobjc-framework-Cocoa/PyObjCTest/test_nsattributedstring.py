from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation

class TestNSAttributedString (TestCase):
    def testOutput(self):
        obj = NSAttributedString.alloc().init()
        m = obj.attributesAtIndex_longestEffectiveRange_inRange_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        m = obj.attribute_atIndex_longestEffectiveRange_inRange_.__metadata__()
        self.failUnless(m['arguments'][4]['type'].startswith('o^'))


if __name__ == '__main__':
    main()
