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
        self.assertIsInstance(v, (int, long))
    def testCreation(self):
        bitset = CFBitVectorCreate(None, [0x11, 0x22, 0x33, 0x44], 30)
        self.assertIsInstance(bitset, CFBitVectorRef)
        self.assertEqual(CFBitVectorGetCount(bitset) , 30)
        set2 = CFBitVectorCreateCopy(None, bitset)
        self.assertIsInstance(set2, CFBitVectorRef)
        self.assertEqual(CFBitVectorGetCount(set2) , 30)
        set3 = CFBitVectorCreateMutableCopy(None, 0, bitset)
        self.assertIsInstance(set3, CFBitVectorRef)
        self.assertEqual(CFBitVectorGetCount(set3) , 30)
        self.assertIsNot(set3, set)
        bitset = CFBitVectorCreateMutable(None, 0)
        self.assertIsInstance(bitset, CFBitVectorRef)
        self.assertEqual(CFBitVectorGetCount(bitset) , 0)
        set2 = CFBitVectorCreateCopy(None, bitset)
        self.assertIsInstance(set2, CFBitVectorRef)
        self.assertEqual(CFBitVectorGetCount(set2) , 0)
        set3 = CFBitVectorCreateMutableCopy(None, 0, bitset)
        self.assertIsInstance(set3, CFBitVectorRef)
        self.assertEqual(CFBitVectorGetCount(set3) , 0)
        self.assertIsNot(set3, set)
    def testInspection(self):
        bitset = CFBitVectorCreate(None, [0x11, 0x22, 0x33, 0x44], 32)

        self.assertEqual( CFBitVectorGetCount(bitset), 32 )
        self.assertEqual( CFBitVectorGetCountOfBit(bitset, (0, 30), 1), 10 )
        self.assertEqual( CFBitVectorGetCountOfBit(bitset, (0, 30), 0), 20 )

        self.assertTrue(  CFBitVectorContainsBit(bitset, (0, 30), 1) )
        self.assertFalse(  CFBitVectorContainsBit(bitset, (0, 3), 1) )

        bits = byte2bits(0x11)
        for i in range(8):
            b = CFBitVectorGetBitAtIndex(bitset, i)
            self.assertEqual(b , bits[i] )
        bits = CFBitVectorGetBits(bitset, (0, 8), None)
        self.assertEqual(bits, b'\x11')

        idx = CFBitVectorGetFirstIndexOfBit(bitset, (0,8), 1)
        self.assertEqual(idx, 3)
        idx = CFBitVectorGetLastIndexOfBit(bitset, (0,8), 1)
        self.assertEqual(idx, 7)

        idx = CFBitVectorGetFirstIndexOfBit(bitset, (0,8), 0)
        self.assertEqual(idx, 0)
        idx = CFBitVectorGetLastIndexOfBit(bitset, (0,8), 0)
        self.assertEqual(idx, 6)

    def testMutation(self):
        bitset = CFBitVectorCreate(None, [0x11, 0x22, 0x33, 0x44], 30)
        bitset = CFBitVectorCreateMutableCopy(None, 0, bitset)

        CFBitVectorSetCount(bitset, 20)
        self.assertEqual(CFBitVectorGetCount(bitset) , 20 )
        bit = CFBitVectorGetBitAtIndex(bitset, 4)
        CFBitVectorFlipBitAtIndex(bitset, 4)
        bit2 = CFBitVectorGetBitAtIndex(bitset, 4)
        self.assertNotEqual(bit , bit2)
        bits = ord(CFBitVectorGetBits(bitset, (0, 8), None))
        CFBitVectorFlipBits(bitset, (0, 8))
        bits2 = ord(CFBitVectorGetBits(bitset, (0, 8), None))

        self.assertEqual(bits2, ~bits & 0xff)

        CFBitVectorSetBitAtIndex(bitset, 4, 0)
        self.assertEqual( CFBitVectorGetBitAtIndex(bitset, 4), 0)
        CFBitVectorSetBitAtIndex(bitset, 4, 1)
        self.assertEqual( CFBitVectorGetBitAtIndex(bitset, 4), 1)

        CFBitVectorSetBits(bitset, (0, 5), 0)
        for i in range(5):
            self.assertEqual( CFBitVectorGetBitAtIndex(bitset, i), 0)
        CFBitVectorSetBits(bitset, (0, 5), 1)
        for i in range(5):
            self.assertEqual( CFBitVectorGetBitAtIndex(bitset, i), 1)

        CFBitVectorSetAllBits(bitset, 1)
        bits = CFBitVectorGetBits(bitset, (0, 20), None)
        self.assertEqual(bits, b'\xff\xff\xf0')
        CFBitVectorSetAllBits(bitset, 0)
        bits = CFBitVectorGetBits(bitset, (0, 20), None)
        self.assertEqual(bits, b'\x00\x00\x00')











if __name__ == "__main__":
    main()
