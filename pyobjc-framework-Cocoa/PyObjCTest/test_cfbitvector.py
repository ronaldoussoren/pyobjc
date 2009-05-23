from PyObjCTools.TestSupport import *
from CoreFoundation import *

def byte2bits(val):
    result = []
    for i in range(7, -1, -1):
        if val & (1 << i):
            result.append(1)
        else:
            result.append(0)
    return result

class TestBitVector (TestCase):
    def testGetTypeID(self):
        v = CFBitVectorGetTypeID()
        self.failUnless(  isinstance(v, (int, long))   )

    def testCreation(self):
        bitset = CFBitVectorCreate(None, [0x11, 0x22, 0x33, 0x44], 30)
        self.failUnless( isinstance(bitset, CFBitVectorRef) )
        self.failUnless(CFBitVectorGetCount(bitset) == 30)

        set2 = CFBitVectorCreateCopy(None, bitset)
        self.failUnless( isinstance(set2, CFBitVectorRef) )
        self.failUnless(CFBitVectorGetCount(set2) == 30)

        set3 = CFBitVectorCreateMutableCopy(None, 0, bitset)
        self.failUnless( isinstance(set3, CFBitVectorRef) )
        self.failUnless(CFBitVectorGetCount(set3) == 30)
        self.failIf(set3 is set)

        bitset = CFBitVectorCreateMutable(None, 0)
        self.failUnless( isinstance(bitset, CFBitVectorRef) )
        self.failUnless(CFBitVectorGetCount(bitset) == 0)

        set2 = CFBitVectorCreateCopy(None, bitset)
        self.failUnless( isinstance(set2, CFBitVectorRef) )
        self.failUnless(CFBitVectorGetCount(set2) == 0)

        set3 = CFBitVectorCreateMutableCopy(None, 0, bitset)
        self.failUnless( isinstance(set3, CFBitVectorRef) )
        self.failUnless(CFBitVectorGetCount(set3) == 0)
        self.failIf(set3 is set)

    def testInspection(self):
        bitset = CFBitVectorCreate(None, [0x11, 0x22, 0x33, 0x44], 30)

        self.failUnlessEqual( CFBitVectorGetCount(bitset), 30 )
        self.failUnlessEqual( CFBitVectorGetCountOfBit(bitset, (0, 30), 1), 10 )
        self.failUnlessEqual( CFBitVectorGetCountOfBit(bitset, (0, 30), 0), 20 )

        self.failUnless(  CFBitVectorContainsBit(bitset, (0, 30), 1) )
        self.failIf(  CFBitVectorContainsBit(bitset, (0, 3), 1) )

        bits = byte2bits(0x11)
        for i in range(8):
            b = CFBitVectorGetBitAtIndex(bitset, i)
            self.failUnless( b ==  bits[i] )

        bits = CFBitVectorGetBits(bitset, (0, 8), None)
        self.assertEquals(bits, chr(0x11))

        idx = CFBitVectorGetFirstIndexOfBit(bitset, (0,8), 1)
        self.assertEquals(idx, 3)
        idx = CFBitVectorGetLastIndexOfBit(bitset, (0,8), 1)
        self.assertEquals(idx, 7)

        idx = CFBitVectorGetFirstIndexOfBit(bitset, (0,8), 0)
        self.assertEquals(idx, 0)
        idx = CFBitVectorGetLastIndexOfBit(bitset, (0,8), 0)
        self.assertEquals(idx, 6)

    def testMutation(self):
        bitset = CFBitVectorCreate(None, [0x11, 0x22, 0x33, 0x44], 30)
        bitset = CFBitVectorCreateMutableCopy(None, 0, bitset)

        CFBitVectorSetCount(bitset, 20)
        self.failUnless( CFBitVectorGetCount(bitset) == 20 )

        bit = CFBitVectorGetBitAtIndex(bitset, 4)
        CFBitVectorFlipBitAtIndex(bitset, 4)
        bit2 = CFBitVectorGetBitAtIndex(bitset, 4)
        self.failIf(bit == bit2)

        bits = ord(CFBitVectorGetBits(bitset, (0, 8), None))
        CFBitVectorFlipBits(bitset, (0, 8))
        bits2 = ord(CFBitVectorGetBits(bitset, (0, 8), None))

        self.assertEquals(bits2, ~bits & 0xff)

        CFBitVectorSetBitAtIndex(bitset, 4, 0)
        self.assertEquals( CFBitVectorGetBitAtIndex(bitset, 4), 0)
        CFBitVectorSetBitAtIndex(bitset, 4, 1)
        self.assertEquals( CFBitVectorGetBitAtIndex(bitset, 4), 1)

        CFBitVectorSetBits(bitset, (0, 5), 0)
        for i in range(5):
            self.assertEquals( CFBitVectorGetBitAtIndex(bitset, i), 0)
        CFBitVectorSetBits(bitset, (0, 5), 1)
        for i in range(5):
            self.assertEquals( CFBitVectorGetBitAtIndex(bitset, i), 1)

        CFBitVectorSetAllBits(bitset, 1)
        bits = CFBitVectorGetBits(bitset, (0, 20), None)
        self.assertEquals(bits, '\xff\xff\xf0')
        CFBitVectorSetAllBits(bitset, 0)
        bits = CFBitVectorGetBits(bitset, (0, 20), None)
        self.assertEquals(bits, '\x00\x00\x00')











if __name__ == "__main__":
    main()
