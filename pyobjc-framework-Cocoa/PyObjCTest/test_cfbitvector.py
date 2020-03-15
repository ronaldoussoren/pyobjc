import CoreFoundation
from PyObjCTools.TestSupport import TestCase


def byte2bits(val):
    result = []
    for i in range(7, -1, -1):
        if val & (1 << i):
            result.append(1)
        else:
            result.append(0)
    return result


class TestBitVector(TestCase):
    def testGetTypeID(self):
        v = CoreFoundation.CFBitVectorGetTypeID()
        self.assertIsInstance(v, int)

    def testCreation(self):
        bitset = CoreFoundation.CFBitVectorCreate(None, [0x11, 0x22, 0x33, 0x44], 30)
        self.assertIsInstance(bitset, CoreFoundation.CFBitVectorRef)
        self.assertEqual(CoreFoundation.CFBitVectorGetCount(bitset), 30)
        set2 = CoreFoundation.CFBitVectorCreateCopy(None, bitset)
        self.assertIsInstance(set2, CoreFoundation.CFBitVectorRef)
        self.assertEqual(CoreFoundation.CFBitVectorGetCount(set2), 30)
        set3 = CoreFoundation.CFBitVectorCreateMutableCopy(None, 0, bitset)
        self.assertIsInstance(set3, CoreFoundation.CFBitVectorRef)
        self.assertEqual(CoreFoundation.CFBitVectorGetCount(set3), 30)
        self.assertIsNot(set3, set)
        bitset = CoreFoundation.CFBitVectorCreateMutable(None, 0)
        self.assertIsInstance(bitset, CoreFoundation.CFBitVectorRef)
        self.assertEqual(CoreFoundation.CFBitVectorGetCount(bitset), 0)
        set2 = CoreFoundation.CFBitVectorCreateCopy(None, bitset)
        self.assertIsInstance(set2, CoreFoundation.CFBitVectorRef)
        self.assertEqual(CoreFoundation.CFBitVectorGetCount(set2), 0)
        set3 = CoreFoundation.CFBitVectorCreateMutableCopy(None, 0, bitset)
        self.assertIsInstance(set3, CoreFoundation.CFBitVectorRef)
        self.assertEqual(CoreFoundation.CFBitVectorGetCount(set3), 0)
        self.assertIsNot(set3, set)

    def testInspection(self):
        bitset = CoreFoundation.CFBitVectorCreate(None, [0x11, 0x22, 0x33, 0x44], 32)

        self.assertEqual(CoreFoundation.CFBitVectorGetCount(bitset), 32)
        self.assertEqual(
            CoreFoundation.CFBitVectorGetCountOfBit(bitset, (0, 30), 1), 10
        )
        self.assertEqual(
            CoreFoundation.CFBitVectorGetCountOfBit(bitset, (0, 30), 0), 20
        )

        self.assertTrue(CoreFoundation.CFBitVectorContainsBit(bitset, (0, 30), 1))
        self.assertFalse(CoreFoundation.CFBitVectorContainsBit(bitset, (0, 3), 1))

        bits = byte2bits(0x11)
        for i in range(8):
            b = CoreFoundation.CFBitVectorGetBitAtIndex(bitset, i)
            self.assertEqual(b, bits[i])
        bits = CoreFoundation.CFBitVectorGetBits(bitset, (0, 8), None)
        self.assertEqual(bits, b"\x11")

        idx = CoreFoundation.CFBitVectorGetFirstIndexOfBit(bitset, (0, 8), 1)
        self.assertEqual(idx, 3)
        idx = CoreFoundation.CFBitVectorGetLastIndexOfBit(bitset, (0, 8), 1)
        self.assertEqual(idx, 7)

        idx = CoreFoundation.CFBitVectorGetFirstIndexOfBit(bitset, (0, 8), 0)
        self.assertEqual(idx, 0)
        idx = CoreFoundation.CFBitVectorGetLastIndexOfBit(bitset, (0, 8), 0)
        self.assertEqual(idx, 6)

    def testMutation(self):
        bitset = CoreFoundation.CFBitVectorCreate(None, [0x11, 0x22, 0x33, 0x44], 30)
        bitset = CoreFoundation.CFBitVectorCreateMutableCopy(None, 0, bitset)

        CoreFoundation.CFBitVectorSetCount(bitset, 20)
        self.assertEqual(CoreFoundation.CFBitVectorGetCount(bitset), 20)
        bit = CoreFoundation.CFBitVectorGetBitAtIndex(bitset, 4)
        CoreFoundation.CFBitVectorFlipBitAtIndex(bitset, 4)
        bit2 = CoreFoundation.CFBitVectorGetBitAtIndex(bitset, 4)
        self.assertNotEqual(bit, bit2)
        bits = ord(CoreFoundation.CFBitVectorGetBits(bitset, (0, 8), None))
        CoreFoundation.CFBitVectorFlipBits(bitset, (0, 8))
        bits2 = ord(CoreFoundation.CFBitVectorGetBits(bitset, (0, 8), None))

        self.assertEqual(bits2, ~bits & 0xFF)

        CoreFoundation.CFBitVectorSetBitAtIndex(bitset, 4, 0)
        self.assertEqual(CoreFoundation.CFBitVectorGetBitAtIndex(bitset, 4), 0)
        CoreFoundation.CFBitVectorSetBitAtIndex(bitset, 4, 1)
        self.assertEqual(CoreFoundation.CFBitVectorGetBitAtIndex(bitset, 4), 1)

        CoreFoundation.CFBitVectorSetBits(bitset, (0, 5), 0)
        for i in range(5):
            self.assertEqual(CoreFoundation.CFBitVectorGetBitAtIndex(bitset, i), 0)
        CoreFoundation.CFBitVectorSetBits(bitset, (0, 5), 1)
        for i in range(5):
            self.assertEqual(CoreFoundation.CFBitVectorGetBitAtIndex(bitset, i), 1)

        CoreFoundation.CFBitVectorSetAllBits(bitset, 1)
        bits = CoreFoundation.CFBitVectorGetBits(bitset, (0, 20), None)
        self.assertEqual(bits, b"\xff\xff\xf0")
        CoreFoundation.CFBitVectorSetAllBits(bitset, 0)
        bits = CoreFoundation.CFBitVectorGetBits(bitset, (0, 20), None)
        self.assertEqual(bits, b"\x00\x00\x00")
