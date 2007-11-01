import sys
import objc.test

import objc
import struct

NSObject = objc.lookUpClass('NSObject')

class OC_TestConveniences(NSObject):
    def initWithHashValue_(self, hashValue):
        self = super(OC_TestConveniences, self).init()
        self.hashValue = hashValue
        return self

    def hash(self):
        return self.hashValue

class TestConveniences(objc.test.TestCase):

    def testHash(self):
        for hashValue in (0, sys.maxint, sys.maxint + 1L, 0xFFFFFFFFL):
            expect = struct.unpack('i', struct.pack('I', hashValue))[0]
            # Python can't hash to -1.  Surprise! :)
            if expect == -1:
                expect = -2
            o = OC_TestConveniences.alloc().initWithHashValue_(hashValue)
            self.assertEquals(o.hash(), hashValue)
            self.assertEquals(hash(o), expect, 'o.hash() == 0x%X | %r != %r' % (o.hash(), hash(o), expect))

if __name__ == '__main__':
    objc.test.main()
