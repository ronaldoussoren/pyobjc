from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSPointerArray (TestCase):
    def testPointers(self):
        o = NSPointerArray.pointerArrayWithStrongObjects()

        m = o.addPointer_.__metadata__()
        self.assertEquals(m['arguments'][2]['type'], '@')

        m = o.insertPointer_atIndex_.__metadata__()
        self.assertEquals(m['arguments'][2]['type'], '@')

        m = o.replacePointerAtIndex_withPointer_.__metadata__()
        self.assertEquals(m['arguments'][3]['type'], '@')

        m = o.pointerAtIndex_.__metadata__()
        self.assertEquals(m['retval']['type'], '@')

if __name__ == "__main__":
    main()
