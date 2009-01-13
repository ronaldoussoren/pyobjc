# This just tests the definitions in the NSKeyedArchiver header
from PyObjCTools.TestSupport import *
from Foundation import *


class TestNSKeyedArchiver (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSInvalidArchiveOperationException, unicode))
        self.failUnless(isinstance(NSInvalidUnarchiveOperationException, unicode))

    def testOutput(self):
        o = NSKeyedUnarchiver.alloc().initForReadingWithData_(
                NSKeyedArchiver.archivedDataWithRootObject_(u"foobar"))
        self.failUnless( isinstance(o, NSKeyedUnarchiver))

        m = o.decodeBytesForKey_returnedLength_.__metadata__()
        self.assertEquals(m['retval']['type'], '^v')
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        data = NSMutableData.alloc().init()
        o = NSArchiver.alloc().initForWritingWithMutableData_(data)
        m = o.encodeBytes_length_forKey_.__metadata__()
        self.assertEquals(m['arguments'][2]['type'], 'n^v')


if __name__ == "__main__":
    main()

